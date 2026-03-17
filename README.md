# mandala-visualizer

**The visual mandala renderer** for the GenesisAeon stack – Climate Dashboard, Cosmic-Web, Mermaid/Grafana integration and fraktal MandalaMap visuals.

[![CI](https://github.com/GenesisAeon/mandala-visualizer/actions/workflows/ci.yml/badge.svg)](https://github.com/GenesisAeon/mandala-visualizer/actions/workflows/ci.yml)
[![Python 3.11+](https://img.shields.io/badge/python-3.11%2B-blue)](https://www.python.org)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![PyPI](https://img.shields.io/pypi/v/mandala-visualizer)](https://pypi.org/project/mandala-visualizer/)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.19076281.svg)](https://doi.org/10.5281/zenodo.19076281)

---

## Install

**DOI**: [10.5281/zenodo.19076281](https://doi.org/10.5281/zenodo.19076281)
**PyPI**: `pip install mandala-visualizer` (oder `pip install "mandala-visualizer[stack]"` für den vollen GenesisAeon-Stack)

```bash
pip install mandala-visualizer
# with full GenesisAeon stack integration:
pip install mandala-visualizer[stack]
```

## CLI Usage

```bash
# Render a Cosmic-Web mandala (saves cosmic-web.png)
mviz render --type cosmic-web

# Render an Entropy-Gate mandala
mviz render --type entropy-gate --output entropy-gate.png

# Render the Climate Entropy Dashboard
mviz dashboard

# Generate Mermaid graph for Grafana
mviz bridge
```

## Python API

```python
from mandala_visualizer import render_mandala, climate_dashboard, mermaid_grafana_bridge

# Render a fractal mandala
fig = render_mandala("cosmic-web")
fig.savefig("mandala.png", dpi=150)

# Climate Dashboard
fig = climate_dashboard()
fig.savefig("dashboard.png", dpi=150)

# Mermaid/Grafana bridge
print(mermaid_grafana_bridge({}))
```

## Project Structure

```
mandala-visualizer/
├── pyproject.toml
├── README.md
├── domains.yaml
├── src/
│   └── mandala_visualizer/
│       ├── __init__.py
│       ├── core.py                  # MandalaMap rendering, Climate Dashboard, Mermaid bridge
│       ├── cli.py                   # mviz CLI (Typer + Rich)
│       └── entropy_table_bridge.py  # Optional entropy-table integration
└── tests/
    ├── test_core.py
    └── test_cli.py
```

## Stack Integration

With `pip install mandala-visualizer[stack]`, mandala-visualizer integrates with the full GenesisAeon stack:

| Package | Role |
|---------|------|
| `utac-core` | β-Fitting and resonance calculations |
| `sigillin` | Sigil-based domain encoding |
| `field-theory` | Field equations for mandala geometry |
| `entropy-table` | Domain relation tracking |
| `cosmic-moment` | Temporal anchoring |

---

Built with [matplotlib](https://matplotlib.org/) · [NetworkX](https://networkx.org/) · [Typer](https://typer.tiangolo.com/) · [Rich](https://rich.readthedocs.io/)
