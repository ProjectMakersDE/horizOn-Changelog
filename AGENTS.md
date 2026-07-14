# horizOn Subproject Bootstrap

This bootstrap applies to Codex, Claude Code, and Gemini in this repository. It is intentionally a regular file: the standalone GitHub Pages checkout cannot resolve links to files outside this repository.

The wiki lives in the parent workspace alongside this repo. Paths below are relative to this file. If your shell sits inside this subproject only and the parent workspace is not checked out, clone the horizOn workspace first.

## Always Read First

1. `../docs/wiki/ops/ai-agent-principles.md`
2. `../docs/wiki/INDEX.md`
3. `../docs/wiki/projects/README.md`
4. `../docs/wiki/projects/horizon-changelog/README.md`

## Workspace Layer

For cross-project infrastructure and shared secrets, use the workspace wiki next to the horizOn workspace. Never hardcode credentials in this repository.

## After The Project README

- Load only the additional files required for the task.
- Use `../docs/wiki/ops/workflows.md` for commit, release, or deployment work.
- Keep product knowledge in the matching wiki folder, not in this bootstrap.
