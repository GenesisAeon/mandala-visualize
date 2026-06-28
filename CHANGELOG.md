# Changelog

## [1.0.0] - 2026

### Added
- Standardized release tooling: `.zenodo.json`, `RELEASE_GUIDE.md`,
  `CONTRIBUTING.md`, issue/PR templates.
- `## Citation` section in README with Zenodo DOI.

### Changed
- Project metadata (`pyproject.toml`) version bumped to `1.0.0` as part of
  the GenesisAeon ecosystem-wide 1.0.0 milestone.
- `entropy-table` dependency pin bumped to `>=2.0.0` and `implosive-genesis`
  to `>=1.0.0` to match their actual released versions.
- **Relicensed from MIT to dual licensing**: source code is now under the
  GNU GPL v3.0-or-later (`LICENSE-CODE`), documentation is now under
  CC BY 4.0 (`LICENSE-DOCS`).

### Fixed
- CI: dropped Python 3.10 from the test matrix (the package requires
  `>=3.11`), added missing `mypy`/type-stub dev dependencies, and fixed
  the docs job to install the `[docs]` extra instead of `[dev]`.

## v0.1.0 (2026-03-17)

- Initial release: fraktale MandalaMap-Rendering (cosmic-web + entropy-gate)
- Climate Entropy Dashboard + Mermaid/Grafana-Bridge
- CLI `mviz render`, `mviz dashboard`, `mviz bridge`
- matplotlib/networkx + uv override-dependencies für [stack]-Extra
- 12/12 tests, 73 % coverage, ruff + mkdocs clean
