# mandala-visualizer

**The visual mandala renderer** for the GenesisAeon stack – Climate Dashboard, Cosmic-Web, Mermaid/Grafana integration and fraktal MandalaMap visuals.

[![CI](https://github.com/GenesisAeon/mandala-visualizer/actions/workflows/ci.yml/badge.svg)](https://github.com/GenesisAeon/mandala-visualizer/actions/workflows/ci.yml)
[![PyPI](https://img.shields.io/pypi/v/mandala-visualizer)](https://pypi.org/project/mandala-visualizer/)
[![Python 3.11+](https://img.shields.io/badge/python-3.11%2B-blue)](https://www.python.org)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://github.com/GenesisAeon/mandala-visualizer/blob/main/LICENSE)
[![Coverage: 73%](https://img.shields.io/badge/coverage-73%25-yellow)](https://github.com/GenesisAeon/mandala-visualizer)

## Install

```bash
pip install mandala-visualizer
# with full GenesisAeon stack integration:
pip install "mandala-visualizer[stack]"
```

## Quickstart

```bash
# Render a Cosmic-Web mandala (saves mandala.png)
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

## Commands

| Command | Description |
|---------|-------------|
| `mviz render` | Render a MandalaMap (cosmic-web or entropy-gate) |
| `mviz dashboard` | Render the Climate Entropy Dashboard |
| `mviz bridge` | Print Mermaid graph for Grafana integration |

## Stack Integration

With `pip install "mandala-visualizer[stack]"`, mandala-visualizer integrates with the full GenesisAeon stack:

| Package | Role |
|---------|------|
| `utac-core` | β-Fitting and resonance calculations |
| `sigillin` | Sigil-based domain encoding |
| `field-theory` | Field equations for mandala geometry |
| `entropy-table` | Domain relation tracking |
| `cosmic-moment` | Temporal anchoring |
| `medium-modulation` | Signal modulation layer |
| `entropy-governance` | Governance and validation |
| `implosive-genesis` | Genesis event processing |

---

Built with [matplotlib](https://matplotlib.org/) · [NetworkX](https://networkx.org/) · [Typer](https://typer.tiangolo.com/) · [Rich](https://rich.readthedocs.io/)
