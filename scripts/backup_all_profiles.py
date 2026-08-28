#!/usr/bin/env python3
"""Back up all Hermes profile configurations without secrets/runtime state."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import sys
from datetime import datetime, timezone

ROOT = Path(os.environ.get("HERMES_DATA_ROOT", "/opt/data")).resolve()
REPO = Path(__file__).resolve().parents[1]
SNAPSHOT_ROOT = REPO / "profiles"
PROFILE_ASSET_DIRS = ("skins", "hooks", "scripts", "desktop-plugins", "tui-widgets", "pets")
IGNORED_NAMES = {
    ".usage.json",
    ".usage.json.lock",
    ".curator_state",
    ".jobs.lock",
    ".tick.lock",
    "__pycache__",
}
SECRET_KEY = re.compile(
    r"^(api[_-]?key|access[_-]?token|auth[_-]?token|bot[_-]?token|app[_-]?token|"
    r"oauth[_-]?token|password|secret|credential|private[_-]?key)$",
    re.IGNORECASE,
)
TOKEN_PATTERNS = (
    (re.compile(rb"github_pat_[A-Za-z0-9_]{20,}"), "GitHub token"),
    (re.compile(rb"gh[pousr]_[A-Za-z0-9]{20,}"), "GitHub token"),
    (re.compile(rb"xox[baprs]-[A-Za-z0-9-]{10,}"), "Slack token"),
    (re.compile(rb"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----"), "private key"),
)


def env_values(profile_home: Path) -> tuple[list[str], list[bytes]]:
    keys: list[str] = []
    values: list[bytes] = []
    env_file = profile_home / ".env"
    if not env_file.exists():
        return keys, values
    for raw in env_file.read_text(errors="replace").splitlines():
        line = raw.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        key = key.strip()
        value = value.strip().strip('"').strip("'")
        if re.fullmatch(r"[A-Za-z_][A-Za-z0-9_]*", key):
            keys.append(key)
            if len(value) >= 8:
                values.append(value.encode())
    return sorted(set(keys)), values


def discover_profiles() -> list[tuple[str, Path]]:
    found: list[tuple[str, Path]] = []
    if (ROOT / "config.yaml").exists():
        found.append(("default", ROOT))
    profiles_dir = ROOT / "profiles"
    if profiles_dir.exists():
        for path in sorted(p for p in profiles_dir.iterdir() if p.is_dir()):
            if (path / "config.yaml").exists() or (path / "SOUL.md").exists():
                if not re.fullmatch(r"[A-Za-z0-9._-]+", path.name):
                    raise RuntimeError(f"Unsafe profile directory name: {path.name!r}")
                found.append((path.name, path))
    return found


def should_ignore(path: Path) -> bool:
    return any(part in IGNORED_NAMES for part in path.parts) or path.suffix in {".pyc", ".lock"}


def copy_tree_filtered(source: Path, destination: Path) -> None:
    if not source.exists():
        return
    for item in source.rglob("*"):
        relative = item.relative_to(source)
        if should_ignore(relative) or item.is_symlink() or not item.is_file():
            continue
        target = destination / relative
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(item, target)


def bundled_skill_names(profile_home: Path) -> set[str]:
    manifest = profile_home / "skills" / ".bundled_manifest"
    if not manifest.exists():
        return set()
    names: set[str] = set()
    for line in manifest.read_text(errors="replace").splitlines():
        if ":" in line:
            names.add(line.split(":", 1)[0].strip())
    return names


def copy_custom_skills(profile_home: Path, destination: Path) -> int:
    skills_root = profile_home / "skills"
    if not skills_root.exists():
        return 0
    bundled = bundled_skill_names(profile_home)
    copied = 0
    for skill_md in sorted(skills_root.rglob("SKILL.md")):
        skill_dir = skill_md.parent
        if skill_dir.name in bundled:
            continue
        relative = skill_dir.relative_to(skills_root)
        copy_tree_filtered(skill_dir, destination / relative)
        copied += 1
    return copied


def safe_config_copy(source: Path, destination: Path) -> None:
    """Copy YAML while redacting a scalar on an explicitly secret-named key."""
    lines: list[str] = []
    for raw in source.read_text(errors="replace").splitlines(keepends=True):
        match = re.match(r"^(\s*)([^#][^:]*):\s*(.*?)\s*(\r?\n)?$", raw)
        if match and SECRET_KEY.fullmatch(match.group(2).strip()) and match.group(3):
            ending = match.group(4) or ""
            raw = f"{match.group(1)}{match.group(2)}: <REDACTED>{ending}"
        lines.append(raw)
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text("".join(lines))


def build_snapshot() -> tuple[list[str], list[bytes]]:
    profiles = discover_profiles()
    staging = REPO / ".profiles.staging"
    if staging.exists():
        shutil.rmtree(staging)
    staging.mkdir(parents=True)
    all_secret_values: list[bytes] = []
    profile_names: list[str] = []
    for name, home in profiles:
        profile_names.append(name)
        destination = staging / name
        destination.mkdir()
        config = home / "config.yaml"
        if config.exists():
            safe_config_copy(config, destination / "config.yaml")
        soul = home / "SOUL.md"
        if soul.exists():
            shutil.copy2(soul, destination / "SOUL.md")
        keys, secret_values = env_values(home)
        all_secret_values.extend(secret_values)
        (destination / "env.example").write_text(
            "# Variable names only. Populate secrets locally; never commit values.\n"
            + "".join(f"{key}=\n" for key in keys)
        )
        manifest = home / "skills" / ".bundled_manifest"
        if manifest.exists():
            shutil.copy2(manifest, destination / "skills.manifest")
        custom_count = copy_custom_skills(home, destination / "custom-skills")
        for directory in PROFILE_ASSET_DIRS:
            copy_tree_filtered(home / directory, destination / directory)
        (destination / "profile-metadata.json").write_text(
            json.dumps(
                {
                    "profile": name,
                    "source": "$HERMES_DATA_ROOT" if name == "default" else f"$HERMES_DATA_ROOT/profiles/{name}",
                    "custom_skills": custom_count,
                },
                indent=2,
            )
            + "\n"
        )
    if SNAPSHOT_ROOT.exists():
        shutil.rmtree(SNAPSHOT_ROOT)
    staging.rename(SNAPSHOT_ROOT)
    active = (ROOT / "active_profile").read_text(errors="replace").strip() if (ROOT / "active_profile").exists() else ""
    system = REPO / "system"
    system.mkdir(exist_ok=True)
    (system / "active_profile").write_text(active + "\n" if active else "")
    return profile_names, all_secret_values


def scan_for_secrets(secret_values: list[bytes]) -> None:
    failures: list[str] = []
    for path in REPO.rglob("*"):
        if not path.is_file() or ".git" in path.parts or path.name == Path(__file__).name:
            continue
        data = path.read_bytes()
        for value in secret_values:
            if value and value in data:
                failures.append(f"{path.relative_to(REPO)}: exact local secret")
        for pattern, label in TOKEN_PATTERNS:
            if pattern.search(data):
                failures.append(f"{path.relative_to(REPO)}: {label}")
    if failures:
        raise RuntimeError("Secret scan failed:\n" + "\n".join(sorted(set(failures))))


def write_metadata(profile_names: list[str]) -> None:
    files = sorted(
        p for p in REPO.rglob("*")
        if p.is_file() and ".git" not in p.parts and p.relative_to(REPO).parts[0] in {"profiles", "system"}
    )
    manifest_dir = REPO / "manifests"
    manifest_dir.mkdir(exist_ok=True)
    metadata_path = manifest_dir / "backup-metadata.json"
    checksums = {
        str(path.relative_to(REPO)): hashlib.sha256(path.read_bytes()).hexdigest() for path in files
    }
    active_profile = (REPO / "system" / "active_profile").read_text().strip()
    created_at = datetime.now(timezone.utc).isoformat(timespec="seconds")
    if metadata_path.exists():
        try:
            previous = json.loads(metadata_path.read_text())
            if (
                previous.get("checksums_sha256") == checksums
                and previous.get("profiles") == profile_names
                and previous.get("active_profile") == active_profile
            ):
                created_at = previous.get("created_at_utc", created_at)
        except (json.JSONDecodeError, OSError):
            pass
    metadata = {
        "created_at_utc": created_at,
        "profile_count": len(profile_names),
        "profiles": profile_names,
        "active_profile": active_profile,
        "scope": "all profile configurations; secrets, memory/session databases, logs, caches, and runtime state excluded",
        "checksums_sha256": checksums,
    }
    metadata_path.write_text(json.dumps(metadata, ensure_ascii=False, indent=2) + "\n")


def git(*args: str, check: bool = True, env: dict[str, str] | None = None) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        ["git", *args], cwd=REPO, text=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, check=check, env=env
    )


def github_token() -> str:
    candidates = [ROOT / "profiles" / "aria" / ".env", ROOT / ".env"]
    candidates.extend(path / ".env" for _, path in discover_profiles())
    for env_file in candidates:
        if not env_file.exists():
            continue
        for raw in env_file.read_text(errors="replace").splitlines():
            line = raw.strip()
            if line and not line.startswith("#") and "=" in line:
                key, value = line.split("=", 1)
                if key.strip() in {"GITHUB_TOKEN", "GH_TOKEN"}:
                    token = value.strip().strip('"').strip("'")
                    if token:
                        return token
    raise RuntimeError("No GITHUB_TOKEN or GH_TOKEN found in a Hermes profile .env")


def askpass(prompt: str) -> int:
    if "username" in prompt.lower():
        print("x-access-token")
    elif "password" in prompt.lower():
        print(github_token())
    return 0


def commit_and_push() -> str:
    git("add", "--all")
    if git("diff", "--cached", "--quiet", check=False).returncode == 0:
        return "NO_CHANGES"
    git("config", "user.name", "bitlabs-ghjo")
    git("config", "user.email", "bitlabs-ghjo@users.noreply.github.com")
    git("commit", "-m", "Back up all Hermes profiles")
    auth_env = os.environ.copy()
    auth_env["GIT_ASKPASS"] = str(Path(__file__).resolve())
    auth_env["GIT_TERMINAL_PROMPT"] = "0"
    git("push", "origin", "main", env=auth_env)
    local = git("rev-parse", "HEAD").stdout.strip()
    remote = git("ls-remote", "origin", "refs/heads/main", env=auth_env).stdout.split()[0]
    if local != remote:
        raise RuntimeError(f"Remote verification failed: local={local}, remote={remote}")
    return local


def main() -> int:
    if len(sys.argv) > 1 and ("username" in sys.argv[1].lower() or "password" in sys.argv[1].lower()):
        return askpass(" ".join(sys.argv[1:]))
    parser = argparse.ArgumentParser()
    parser.add_argument("--no-push", action="store_true", help="Build and scan the snapshot without committing/pushing")
    args = parser.parse_args()
    names, values = build_snapshot()
    scan_for_secrets(values)
    write_metadata(names)
    scan_for_secrets(values)
    result = "NOT_PUSHED" if args.no_push else commit_and_push()
    print(json.dumps({"status": "ok", "profiles": names, "profile_count": len(names), "git": result}))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
