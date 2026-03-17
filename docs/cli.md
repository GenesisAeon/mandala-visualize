# CLI Reference

The `mviz` CLI provides three commands for rendering mandalas, dashboards, and generating Mermaid graphs.

---

## `mviz render`

Render a fraktal MandalaMap and save it as a PNG file.

```
Usage: mviz render [OPTIONS]

Options:
  --type TEXT    Mandala type: cosmic-web or entropy-gate  [default: cosmic-web]
  --output PATH  Output PNG file path  [default: mandala.png]
  --help         Show this message and exit.
```

**Examples**

```bash
# Render the default cosmic-web mandala
mviz render

# Render an entropy-gate mandala
mviz render --type entropy-gate

# Custom output path
mviz render --type cosmic-web --output my-mandala.png
```

---

## `mviz dashboard`

Render the Climate Entropy Dashboard (entropy wave + fractal mandala pattern) and save as PNG.

```
Usage: mviz dashboard [OPTIONS]

Options:
  --output PATH  Output PNG file path  [default: climate-dashboard.png]
  --help         Show this message and exit.
```

**Examples**

```bash
# Render dashboard with default output name
mviz dashboard

# Custom output path
mviz dashboard --output my-dashboard.png
```

---

## `mviz bridge`

Print a Mermaid graph string for Grafana integration. The output can be pasted directly into a Grafana Mermaid panel.

```
Usage: mviz bridge [OPTIONS]

Options:
  --help  Show this message and exit.
```

**Example output**

```
graph TD
  A[Entropy] --> B[Governance]
  B --> C[Cosmic Moment]
  C --> D[MandalaMap]
  D --> A
```

```bash
# Print Mermaid graph to stdout
mviz bridge

# Pipe to file for Grafana import
mviz bridge > grafana-mandala.mmd
```
