# horizOn Changelog

Public changelog for the [horizOn](https://horizon.pm) platform by [ProjectMakers](https://projectmakers.de).

Live site: **[changelog.horizon.pm](https://changelog.horizon.pm)**

## Changelogs

| Product | Page | Source file |
|---------|------|-------------|
| Dashboard (web frontend) | [changelog.horizon.pm/dashboard-changelog](https://changelog.horizon.pm/dashboard-changelog) | [dashboard-changelog.md](dashboard-changelog.md) |
| Server (backend API) | [changelog.horizon.pm/server-changelog](https://changelog.horizon.pm/server-changelog) | [server-changelog.md](server-changelog.md) |
| Godot SDK | [changelog.horizon.pm/godot-sdk-changelog](https://changelog.horizon.pm/godot-sdk-changelog) | [godot-sdk-changelog.md](godot-sdk-changelog.md) |
| Unity SDK | [changelog.horizon.pm/unity-sdk-changelog](https://changelog.horizon.pm/unity-sdk-changelog) | [unity-sdk-changelog.md](unity-sdk-changelog.md) |
| Unreal SDK | [changelog.horizon.pm/unreal-sdk-changelog](https://changelog.horizon.pm/unreal-sdk-changelog) | [unreal-sdk-changelog.md](unreal-sdk-changelog.md) |
| Simple Server (self-hosted) | [changelog.horizon.pm/simple-server-changelog](https://changelog.horizon.pm/simple-server-changelog) | [simple-server-changelog.md](simple-server-changelog.md) |
| MCP Server | [changelog.horizon.pm/mcp-server-changelog](https://changelog.horizon.pm/mcp-server-changelog) | [mcp-server-changelog.md](mcp-server-changelog.md) |

## How the changelogs are updated

The files are generated, do not edit them by hand. The
[Sync and Publish Changelogs](.github/workflows/sync-changelogs.yml) workflow
runs when a product repository sends a `sync-changelog` dispatch after a
release, on every push to `master` and on manual start. It reads each
product's semantic-release `CHANGELOG.md`, runs it through
[scripts/clean_changelog.py](scripts/clean_changelog.py) and deploys the site
to GitHub Pages.

The published changelogs list features, bug fixes, performance improvements
and security fixes. Internal entries (CI, tests, build, chores, refactoring),
internal ticket numbers and links into private repositories are left out.

## Feedback

Use the issue templates to:

- [Report a bug](https://github.com/ProjectMakersDE/horizOn-Changelog/issues/new?template=bug_report.yml)
- [Request a feature](https://github.com/ProjectMakersDE/horizOn-Changelog/issues/new?template=feature_request.yml)

## About horizOn

horizOn is a backend platform for game developers and app creators, with user
management, API key management, analytics and more, plus SDKs for Godot, Unity
and Unreal. Learn more at [horizon.pm](https://horizon.pm).

## License

[MIT](LICENSE)
