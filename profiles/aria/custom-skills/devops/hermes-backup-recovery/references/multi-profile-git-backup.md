# Multi-profile Git backup implementation checklist

Use this reference when turning the SKILL.md workflow into a deterministic script.

## Discovery model

Treat two locations as profile homes:

1. `<data-root>` as `default` when `config.yaml` exists.
2. Every direct child of `<data-root>/profiles/` containing `config.yaml` or `SOUL.md`.

Validate profile directory names before using them as destination paths. A conservative portable pattern is `[A-Za-z0-9._-]+`.

## Recommended repository layout

```text
.gitignore
README.md
profiles/
  default/
    config.yaml
    SOUL.md
    env.example
    skills.manifest
    custom-skills/
    profile-metadata.json
  <name>/
system/
  active_profile
manifests/
  backup-metadata.json
scripts/
  backup_all_profiles.py
```

Build `profiles/` in a staging directory, then replace the prior snapshot only after collection succeeds. Do not follow symlinks.

## Deterministic metadata

For every profile/system file, calculate SHA-256 and store it under its repository-relative path. Before writing a new generation timestamp, compare:

- checksums
- ordered profile list
- active-profile value

If all are unchanged, preserve the previous timestamp. This makes the Git index clean on a no-op run.

## Secret scan

Collect `.env` values in memory without printing them. Ignore empty/short values for exact matching, but retain all valid variable names for `env.example`.

Before `git add`, scan every candidate output for:

- Every exact source secret value of meaningful length
- `github_pat_...` and `gh[pousr]_...`
- Slack `xox...` tokens
- PEM private-key headers
- Populated scalar fields whose key is explicitly secret-named

Scan again after metadata generation. Exit nonzero and do not stage anything on a match.

Avoid broad substring rules such as any key containing `token`; legitimate settings like token counts create false positives. Match complete sensitive key names instead.

## Fine-grained PAT push without leaking it

Prefer an authenticated `gh` installation when available. Otherwise use `GIT_ASKPASS`:

1. The helper prints a fixed username such as `x-access-token` for the username prompt.
2. It reads `GITHUB_TOKEN`/`GH_TOKEN` from a local profile `.env` only for the password prompt.
3. Set `GIT_TERMINAL_PROMPT=0` so failures stop rather than block.
4. Never place the token in the remote URL, command text, logs, or repository files.

After pushing, run authenticated `git ls-remote origin refs/heads/main` and compare the returned SHA with local `HEAD`.

## Cron wrapper

Hermes cron accepts script names relative to the active profile's `scripts/` directory. Put a small executable wrapper there that `exec`s the versioned repository script. Schedule the wrapper filename, not an absolute path.

Use script-only/no-agent mode for deterministic backups. Read the job back after creation and verify its enabled state and next-run time. Directly run the wrapper once before scheduling it.

## Public repository boundary

Even perfect token scanning does not remove privacy risk. Public backups should exclude:

- memory/user-profile text
- sessions and response stores
- channel directories and routing state
- logs and job execution databases
- auth pools and `.env`

A request for “all profiles” should expand profile discovery, not silently broaden the data classification boundary.
