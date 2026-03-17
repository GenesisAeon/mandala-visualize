# API Reference

## `render_mandala`

```python
from mandala_visualizer import render_mandala

fig = render_mandala(type="cosmic-web")
fig.savefig("mandala.png", dpi=150)
```

**Parameters:**

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `type` | `"cosmic-web"` \| `"entropy-gate"` | `"cosmic-web"` | Mandala type to render |

**Returns:** `matplotlib.figure.Figure`

---

## `climate_dashboard`

```python
from mandala_visualizer import climate_dashboard

fig = climate_dashboard()
fig.savefig("dashboard.png", dpi=150)
```

Renders a two-panel Climate Entropy Dashboard: entropy wave (golden ratio φ = 1.618) and a fractal mandala polar pattern.

**Returns:** `matplotlib.figure.Figure`

---

## `mermaid_grafana_bridge`

```python
from mandala_visualizer import mermaid_grafana_bridge

print(mermaid_grafana_bridge({}))
```

Generates a Mermaid graph string for Grafana panel integration (Entropy → Governance → Cosmic Moment → MandalaMap cycle).

**Parameters:**

| Parameter | Type | Description |
|-----------|------|-------------|
| `data` | `dict` | Reserved for future use |

**Returns:** `str` (Mermaid graph definition)

---

## `bind_to_utac`

```python
from mandala_visualizer.core import bind_to_utac

result = bind_to_utac(beta=0.0625)
```

Optional binding to `utac-core` β-Fitting. Falls back gracefully if the stack is not installed.

**Parameters:**

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `beta` | `float` | `0.0625` | Beta fitting parameter |

**Returns:** `str`
