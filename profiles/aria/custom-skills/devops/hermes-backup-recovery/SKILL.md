---
name: hermes-backup-recovery
description: "Use when backing up or restoring Hermes profiles safely."
version: 1.0.0
author: Hermes Agent
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [hermes, backup, restore, profiles, github, cron, security]
---

# Hermes Backup and Recovery

Back up Hermes configuration across the default data root and every named profile without leaking credentials, session history, or runtime databases.

## When to Use

Use this skill for:

- One-time or recurring Hermes configuration backups
- Multi-profile migration and disaster-recovery preparation
- GitHub/Git-backed profile snapshots
- Auditing whether a backup excludes secrets and runtime state
- Restoring default and named Hermes profiles on a new installation

## Scope Decision First

1. Resolve the Hermes data root from the live environment; prefer `$HERMES_HOME` for the active profile and identify the installation data root separately.
2. Treat the data root itself as the **default profile** when it contains `config.yaml`.
3. Discover named profiles dynamically under `<data-root>/profiles/<name>`; never hardcode only the currently active profile.
4. Determine repository visibility before selecting content:
   - Public repository: configuration allowlist only; exclude memories and identifiers by default.
   - Private encrypted backup: broader state may be considered, but credentials still require explicit handling.
5. State clearly that “all profiles” does not automatically mean “all runtime data.”

## Safe Configuration Allowlist

Back up per profile:

- `config.yaml`, with explicitly secret-named scalar fields redacted or rejected
- `SOUL.md`
- An `env.example` containing variable names only
- Installed-skill manifest/version hashes
- Non-bundled user-created skills after secret scanning
- User customization directories when present: `skins`, `hooks`, `scripts`, `desktop-plugins`, `tui-widgets`, `pets`

Back up system-level profile selection separately, such as `active_profile`.

Exclude by default:

- `.env`, `auth.json`, OAuth pools, tokens, private keys, credential stores
- Session, response, execution, memory, and kanban databases
- Logs, caches, PID/socket/lock files, temporary workspaces
- Channel routing files and user/platform identifiers in public repositories
- Generated backups and cache manifests that do not aid recovery

## Procedure

1. **Inspect safely.** Enumerate profile names and file counts without printing secret values. Report environment-variable names only.
2. **Confirm the target.** Verify the exact Git remote URL and push branch. A token may read public repositories that it cannot write; successful listing is not proof of scoped write access.
3. **Build a deterministic snapshot.** Use a structure such as:

   ```text
   profiles/default/
   profiles/<name>/
   system/active_profile
   manifests/backup-metadata.json
   scripts/backup_all_profiles.py
   ```

4. **Generate secret-free environment templates.** Parse each `.env` locally, retain valid variable names, and discard values.
5. **Scan before staging.** At minimum:
   - Compare every output file against exact nontrivial values loaded from all source `.env` files.
   - Detect known GitHub/Slack token prefixes and PEM private-key headers.
   - Reject or redact populated YAML/JSON keys explicitly named `api_key`, `access_token`, `password`, `secret`, `credential`, or `private_key`.
6. **Keep runs idempotent.** Preserve metadata timestamps when profile contents and checksums are unchanged so recurring runs produce no empty daily commits.
7. **Commit and push securely.** Never embed a PAT in a remote URL or print it. When `gh` is unavailable, use an ephemeral `GIT_ASKPASS` helper that reads the token locally and returns it only to Git.
8. **Verify external state.** Compare local `HEAD` with the remote branch SHA and enumerate the remote tree before claiming success.
9. **Automate only after a direct successful run.** Test the exact wrapper first, then schedule it.

## Hermes Cron Integration

Hermes cron script paths are restricted to the active profile's `scripts/` directory. Install a small executable wrapper there and configure the cron job with the **relative filename only**, not an absolute or home-relative path.

For a script-only backup job:

- Use `no_agent=true`.
- Let empty or concise stdout represent the result.
- Store job output locally unless an explicit gateway delivery target is requested.
- Read the cron job back after creation and verify `enabled`, `schedule`, `script`, and `next_run_at`.
- The wrapper should exit nonzero on secret-scan, Git push, or remote-verification failure.

## Restore Verification

A backup is not useful until its recovery path is explicit:

1. Recreate the default and named profile directories.
2. Restore allowlisted files to their corresponding homes.
3. Recreate `.env` files manually from `env.example`; never infer missing secret values.
4. Reinstall bundled skills from their manifests; restore custom skills and customization directories.
5. Restore active-profile selection.
6. Run Hermes configuration validation and start a fresh session.
7. Confirm provider authentication separately because credentials are intentionally absent.

## Pitfalls

- Backing up only `$HERMES_HOME` misses the default root and sibling profiles.
- Copying all of a profile recursively leaks `.env`, auth pools, sessions, or databases.
- GitHub `/user/repos` output includes public repositories and does not prove fine-grained-token write scope.
- `Authorization: Bearer` passed as a Git HTTP extra header may not satisfy smart-HTTP credential negotiation; a non-logging `GIT_ASKPASS` helper is the safer fallback.
- Timestamp-only metadata changes create meaningless recurring commits.
- An absolute script path in a Hermes cron job is rejected; use a relative filename under the active profile's `scripts/` directory.
- A public backup repository makes memory text and channel identifiers public even when they contain no token-shaped secrets.

## Detailed Implementation Notes

See `references/multi-profile-git-backup.md` for a condensed implementation and verification checklist.
