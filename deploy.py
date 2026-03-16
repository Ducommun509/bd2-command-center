#!/usr/bin/env python3
"""
BD2 Command Center — One-command deploy script.

Usage:
    python3 deploy.py                     # auto-generates commit message
    python3 deploy.py "your message"      # custom commit message
    python3 deploy.py --status            # check deploy status
"""

import subprocess
import sys
import os
from datetime import datetime


def run(cmd, capture=False):
    """Run a shell command."""
    result = subprocess.run(cmd, shell=True, capture_output=capture, text=True)
    if capture:
        return result.stdout.strip(), result.returncode
    return result.returncode


def get_changes():
    """Get a summary of changed files."""
    out, _ = run("git diff --stat", capture=True)
    return out


def main():
    # Ensure we're in the repo directory
    script_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(script_dir)

    # Check for --status flag
    if len(sys.argv) > 1 and sys.argv[1] == "--status":
        print("\n📊 Checking deployment status...")
        out, _ = run("git log --oneline -5", capture=True)
        print(f"\nRecent commits:\n{out}")
        branch, _ = run("git branch --show-current", capture=True)
        remote, _ = run("git remote get-url origin", capture=True)
        print(f"\nBranch: {branch}")
        print(f"Remote: {remote}")
        print(f"Pages URL: https://ducommun509.github.io/bd2-command-center/")
        return

    # Check for uncommitted changes
    changes = get_changes()
    if not changes:
        status, _ = run("git status --porcelain", capture=True)
        if not status:
            print("✅ Nothing to deploy — everything is up to date.")
            return

    # Show what's being deployed
    print("\n⚡ BD2 Command Center — Deploy\n")
    print("Changes:")
    status, _ = run("git status --short", capture=True)
    print(status)

    # Build commit message
    if len(sys.argv) > 1 and sys.argv[1] != "--status":
        msg = " ".join(sys.argv[1:])
    else:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
        msg = f"BD2 update — {timestamp}"

    # Stage, commit, push
    print(f"\n📦 Committing: {msg}")
    run("git add -A")

    ret = run(f'git commit -m "{msg}"')
    if ret != 0:
        print("❌ Commit failed.")
        return

    print("🚀 Pushing to GitHub...")
    ret = run("git push")
    if ret != 0:
        print("❌ Push failed. Check your credentials.")
        print("   You may need a Personal Access Token: github.com/settings/tokens")
        return

    print("\n✅ Deployed! Live in ~1 min at:")
    print("   https://ducommun509.github.io/bd2-command-center/")


if __name__ == "__main__":
    main()
