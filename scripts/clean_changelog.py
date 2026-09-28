#!/usr/bin/env python3
"""Turn a semantic-release CHANGELOG.md into the public changelog text.

Reads Markdown on stdin and writes the cleaned Markdown to stdout.

Rules:
- Only Features, Bug Fixes, Performance Improvements, Reverts, Security and
  BREAKING CHANGES sections are published. Entries scoped to ci, test, tests,
  chore or build are dropped from those sections too.
- Links into ProjectMakersDE repositories that are not public are removed.
  Version headings keep their number, entries keep their text.
- Internal ticket references (TASK-123) are removed.
- A release left without entries gets a short maintenance note, so every
  released version stays listed. Entries that become identical are listed once.

Repository visibility is looked up with `gh api` (uses GH_TOKEN). A repository
counts as public only when the API says so; errors count as private.
"""

import re
import subprocess
import sys
from functools import lru_cache

OWNER = "ProjectMakersDE"
PUBLISHED_SECTIONS = {
    "features",
    "bug fixes",
    "performance improvements",
    "reverts",
    "security",
    "breaking changes",
}
INTERNAL_SCOPES = {"ci", "test", "tests", "chore", "build"}
EMPTY_RELEASE_NOTE = "Maintenance release without user-facing changes."

VERSION_HEADING = re.compile(r"^#{1,2} \[?\d+\.\d+\.\d+")
TOP_HEADING = re.compile(r"^#{1,2} ")
SECTION_HEADING = re.compile(r"^### (.+?)\s*$")
ENTRY = re.compile(r"^\* ")
ENTRY_SCOPE = re.compile(r"^\* \*\*([^*]+?):\*\*")
REPO_URL = re.compile(
    r"https?://github\.com/" + OWNER + r"/([A-Za-z0-9._-]+)", re.IGNORECASE
)
LINK = r"\[([^\]]*)\]\((https?://github\.com/" + OWNER + r"/[^)\s]+)\)"
PAREN_LINK = re.compile(r"\s*\(" + LINK + r"\)", re.IGNORECASE)
CLOSES_LINKS = re.compile(
    r",?\s*closes(?:\s*,?\s*" + LINK + r")+", re.IGNORECASE
)
ANY_LINK = re.compile(LINK, re.IGNORECASE)
TICKET_PAREN = re.compile(r"\s*\([^()]*\bTASK-\d+[^()]*\)")
TICKET = re.compile(r"\bTASK-\d+(?:/\d+)?\b[ \t]*")


@lru_cache(maxsize=None)
def is_public(repo):
    try:
        result = subprocess.run(
            ["gh", "api", f"repos/{OWNER}/{repo}", "--jq", ".private"],
            capture_output=True,
            text=True,
            timeout=60,
        )
    except (OSError, subprocess.SubprocessError):
        return False
    return result.returncode == 0 and result.stdout.strip() == "false"


def url_is_public(url):
    match = REPO_URL.match(url)
    return bool(match) and is_public(match.group(1))


def strip_private_links(line):
    def drop_paren(match):
        return match.group(0) if url_is_public(match.group(2)) else ""

    def drop_closes(match):
        urls = re.findall(r"\((https?://[^)\s]+)\)", match.group(0))
        return match.group(0) if all(url_is_public(u) for u in urls) else ""

    def unlink(match):
        text, url = match.group(1), match.group(2)
        if url_is_public(url):
            return match.group(0)
        # Issue numbers and commit hashes mean nothing without the link.
        if re.fullmatch(r"#\w+|[0-9a-f]{7,40}", text):
            return ""
        return text

    line = PAREN_LINK.sub(drop_paren, line)
    line = CLOSES_LINKS.sub(drop_closes, line)
    return ANY_LINK.sub(unlink, line)


def strip_tickets(line):
    if "TASK-" not in line:
        return line
    line = TICKET_PAREN.sub("", line)
    line = TICKET.sub("", line)
    line = re.sub(r"(\*\*[^*]+:\*\*) +", r"\1 ", line)
    line = re.sub(r"^\* {2,}", "* ", line)
    return re.sub(r" {2,}", " ", line).rstrip()


def clean_line(line):
    return strip_tickets(strip_private_links(line))


def split_blocks(lines):
    """Group lines into (kind, lines) blocks: heading, section, entry, other."""
    blocks = []
    for line in lines:
        if TOP_HEADING.match(line):
            blocks.append(["heading", [line]])
        elif SECTION_HEADING.match(line):
            blocks.append(["section", [line]])
        elif ENTRY.match(line):
            blocks.append(["entry", [line]])
        elif line.startswith((" ", "\t")) and line.strip() and blocks and blocks[-1][0] == "entry":
            blocks[-1][1].append(line)
        else:
            blocks.append(["other", [line]])
    return blocks


def entry_is_internal(first_line):
    match = ENTRY_SCOPE.match(first_line)
    if not match:
        return False
    scopes = {s.strip().lower() for s in re.split(r"[,/]", match.group(1))}
    return scopes <= INTERNAL_SCOPES


def filter_blocks(blocks):
    out = []
    in_version = False
    version_has_entries = False
    section_published = True
    pending_section = None
    seen_entries = set()

    def close_version():
        if in_version and not version_has_entries:
            out.append(["other", [EMPTY_RELEASE_NOTE]])
            out.append(["other", [""]])

    for kind, lines in blocks:
        if kind == "heading":
            close_version()
            in_version = bool(VERSION_HEADING.match(lines[0]))
            version_has_entries = False
            section_published = True
            pending_section = None
            out.append([kind, lines])
        elif kind == "section":
            name = SECTION_HEADING.match(lines[0]).group(1).strip().lower()
            section_published = name in PUBLISHED_SECTIONS
            seen_entries = set()
            # Hold the heading back until the section has a published entry.
            pending_section = [kind, lines] if section_published else None
        elif kind == "entry":
            if not section_published or entry_is_internal(lines[0]):
                continue
            # Two commits with the same message look identical once the
            # commit links are gone.
            if tuple(lines) in seen_entries:
                continue
            seen_entries.add(tuple(lines))
            if pending_section:
                out.append(pending_section)
                out.append(["other", [""]])
                pending_section = None
            version_has_entries = True
            out.append([kind, lines])
        else:
            if not section_published:
                continue
            if pending_section:
                if not lines[0].strip():
                    continue
                out.append(pending_section)
                out.append(["other", [""]])
                pending_section = None
                version_has_entries = True
            out.append([kind, lines])
    close_version()
    return out


def clean(text):
    lines = [clean_line(line) for line in text.split("\n")]
    blocks = filter_blocks(split_blocks(lines))
    output = "\n".join(line for _, block_lines in blocks for line in block_lines)
    output = re.sub(r"\n{4,}", "\n\n\n", output)
    return output


def main():
    sys.stdout.write(clean(sys.stdin.read()))


if __name__ == "__main__":
    main()
