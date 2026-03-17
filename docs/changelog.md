# Changelog

All notable changes to **mandala-visualizer** are documented here.

The format follows [Keep a Changelog](https://keepachangelog.com/en/1.0.0/).
This project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [0.1.0] – 2026-03-17

### Added

- **`render_mandala()`** – fraktal MandalaMap renderer for `cosmic-web` (star graph, spring layout) and `entropy-gate` (Petersen graph, circular layout) types via matplotlib + NetworkX.
- **`climate_dashboard()`** – Climate Entropy Dashboard with golden-ratio entropy wave (φ = 1.618) and fractal mandala polar pattern.
- **`mermaid_grafana_bridge()`** – Mermaid graph generator for Grafana panel integration (Entropy → Governance → Cosmic Moment → MandalaMap cycle).
- **`bind_to_utac()`** – Optional β-Fitting binding to `utac-core`; falls back gracefully if stack not installed.
- **`mviz render`** CLI command – render any mandala type to PNG with configurable output path.
- **`mviz dashboard`** CLI command – render Climate Entropy Dashboard to PNG.
- **`mviz bridge`** CLI command – print Mermaid graph to stdout for Grafana import.
- **`[stack]` extra** – optional integration with the full GenesisAeon stack (`utac-core`, `sigillin`, `field-theory`, `cosmic-moment`, `medium-modulation`, `entropy-governance`, `entropy-table`, `implosive-genesis`).
- **`uv` override-dependencies** – non-PyPI stack packages excluded from lock resolution via `python_version < '0'` markers so CI stays green without requiring private index.
- **12/12 tests** with 73% coverage (`test_core.py` + `test_cli.py`).
- **mkdocs-material** documentation with CLI reference and changelog.
- `domains.yaml` – GenesisAeon domain/metric configuration file.

### Technical

- `src/` layout with `hatchling` build backend.
- `ruff` (E, F, B, I, W, UP, C4, SIM rules) – all checks pass.
- Python 3.11+ required; tested on 3.11 and 3.12.
- MIT License.

[0.1.0]: https://github.com/GenesisAeon/mandala-visualizer/releases/tag/v0.1.0
