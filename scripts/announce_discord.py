#!/usr/bin/env python3
"""Post every newly published release to the horizOn Discord announcement channel.

Usage: announce_discord.py <before-ref> <after-ref>

Compares the public changelog files between two commits of this repository.
Each version heading that exists after and not before is one new release, and
its section is sent as one embed to the webhook in DISCORD_CHANGELOG_WEBHOOK.

Without the variable the script only lists what it would send, so a fork or a
run before the webhook exists stays green. A webhook that answers with an error
fails the run, so a broken announcement is visible in the workflow.
"""

import json
import os
import re
import subprocess
import sys
import time
import urllib.error
import urllib.request

SITE = "https://changelog.horizon.pm"
PRODUCTS = [
    ("dashboard-changelog.md", "Dashboard"),
    ("server-changelog.md", "Server API"),
    ("unity-sdk-changelog.md", "Unity SDK"),
    ("godot-sdk-changelog.md", "Godot SDK"),
    ("unreal-sdk-changelog.md", "Unreal SDK"),
    ("mcp-server-changelog.md", "MCP Server"),
    ("simple-server-changelog.md", "simpleServer"),
]
# A release burst (for example a first run) posts at most this many versions per product.
MAX_RELEASES_PER_PRODUCT = 3
EMBED_LIMIT = 3900
COLOR = 0x2563EB

VERSION_HEADING = re.compile(r"^#{1,2} \[?(\d+\.\d+\.\d+)\]?(?:\([^)]*\))?\s*(?:\((\d{4}-\d{2}-\d{2})\))?")


def file_at(ref, path):
    result = subprocess.run(["git", "show", f"{ref}:{path}"], capture_output=True, text=True)
    return result.stdout if result.returncode == 0 else ""


def releases(markdown):
    """Version sections in file order: (version, date, body)."""
    found = []
    current = None
    for line in markdown.splitlines():
        match = VERSION_HEADING.match(line)
        if match:
            if current:
                found.append(current)
            current = [match.group(1), match.group(2) or "", []]
        elif current:
            current[2].append(line)
    if current:
        found.append(current)
    return [(version, date, "\n".join(body).strip()) for version, date, body in found]


def to_discord(body):
    """Discord renders no ### headings inside embeds, so section titles become bold lines."""
    lines = [re.sub(r"^#{3,} (.+)$", r"**\1**", line) for line in body.splitlines()]
    text = re.sub(r"\n{3,}", "\n\n", "\n".join(lines)).strip()
    if len(text) > EMBED_LIMIT:
        text = text[:EMBED_LIMIT].rsplit("\n", 1)[0] + "\n..."
    return text


def new_releases(before, after):
    announcements = []
    for path, name in PRODUCTS:
        known = {version for version, _, _ in releases(file_at(before, path))}
        fresh = [r for r in releases(file_at(after, path)) if r[0] not in known]
        for version, date, body in reversed(fresh[:MAX_RELEASES_PER_PRODUCT]):
            page = path.replace(".md", ".html")
            announcements.append({
                "title": f"horizOn {name} {version}",
                "url": f"{SITE}/{page}",
                "description": to_discord(body) or "Maintenance release without user-facing changes.",
                "color": COLOR,
                "footer": {"text": f"Released {date}" if date else "horizOn changelog"},
            })
    return announcements


def post(webhook, embed):
    payload = json.dumps({"username": "horizOn Changelog", "embeds": [embed]}).encode()
    request = urllib.request.Request(
        webhook, data=payload, method="POST",
        headers={"Content-Type": "application/json", "User-Agent": "horizOn-Changelog"},
    )
    for attempt in range(3):
        try:
            with urllib.request.urlopen(request, timeout=20):
                return
        except urllib.error.HTTPError as error:
            # Discord rate limit: wait as told and try again, every other error fails the run.
            if error.code == 429 and attempt < 2:
                time.sleep(float(json.loads(error.read() or b"{}").get("retry_after", 2)))
                continue
            raise SystemExit(f"Discord webhook answered HTTP {error.code} for {embed['title']}")


def main():
    if len(sys.argv) != 3:
        raise SystemExit(__doc__)
    before, after = sys.argv[1], sys.argv[2]
    announcements = new_releases(before, after)
    if not announcements:
        print("No new releases to announce")
        return
    webhook = os.environ.get("DISCORD_CHANGELOG_WEBHOOK", "").strip()
    for embed in announcements:
        if webhook:
            post(webhook, embed)
            print(f"Announced {embed['title']}")
            time.sleep(1)
        else:
            print(f"DISCORD_CHANGELOG_WEBHOOK not set, would announce {embed['title']}")


if __name__ == "__main__":
    main()
