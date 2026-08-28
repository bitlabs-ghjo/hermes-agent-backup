#!/usr/bin/env python3
"""Cron entry point for the all-profile GitHub backup."""

import os
from pathlib import Path

script = Path('/opt/data/profiles/aria/workspace/hermes-agent-backup/scripts/backup_all_profiles.py')
if not script.exists():
    raise SystemExit(f'Backup script not found: {script}')
os.execv(str(script), [str(script)])
