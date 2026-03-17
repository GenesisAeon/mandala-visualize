"""CLI entry point for mandala-visualizer (mviz)."""

from __future__ import annotations

from pathlib import Path
from typing import Annotated

import typer
from rich.console import Console

from .core import climate_dashboard, mermaid_grafana_bridge, render_mandala

app = typer.Typer(
    name="mviz",
    help="Mandala-Visualizer CLI – fraktal visuals, dashboards, Mermaid bridges.",
    add_completion=False,
)
console = Console()


@app.command()
def render(
    type: Annotated[
        str, typer.Option(help="Mandala type: cosmic-web or entropy-gate")
    ] = "cosmic-web",
    output: Annotated[Path, typer.Option(help="Output PNG file path")] = Path(
        "mandala.png"
    ),
) -> None:
    """Render a MandalaMap and save it as a PNG."""
    fig = render_mandala(type)  # type: ignore[arg-type]
    fig.savefig(output, dpi=150)
    console.print(f"[bold green]Rendered '{type}' mandala → {output}[/]")


@app.command()
def dashboard(
    output: Annotated[Path, typer.Option(help="Output PNG file path")] = Path(
        "climate-dashboard.png"
    ),
) -> None:
    """Render the Climate Entropy Dashboard and save it as a PNG."""
    fig = climate_dashboard()
    fig.savefig(output, dpi=150)
    console.print(f"[bold cyan]Climate Dashboard rendered → {output}[/]")


@app.command()
def bridge() -> None:
    """Print a Mermaid graph string for Grafana integration."""
    mermaid = mermaid_grafana_bridge({})
    console.print("[bold magenta]Mermaid code:[/]")
    console.print(mermaid)


if __name__ == "__main__":
    app()
