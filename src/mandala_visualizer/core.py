"""Core rendering functions for MandalaMap, Climate Dashboard, and Mermaid bridge."""

from __future__ import annotations

from typing import Literal

import matplotlib.pyplot as plt
import networkx as nx
import numpy as np


def render_mandala(
    type: Literal["cosmic-web", "entropy-gate"] = "cosmic-web",
) -> plt.Figure:
    """Render a fraktal MandalaMap.

    Args:
        type: The mandala type – ``"cosmic-web"`` (default) or ``"entropy-gate"``.

    Returns:
        A :class:`matplotlib.figure.Figure` containing the rendered mandala.
    """
    fig, ax = plt.subplots(figsize=(8, 8))
    if type == "cosmic-web":
        G = nx.star_graph(20)
        pos = nx.spring_layout(G, seed=42)
        nx.draw(
            G,
            pos=pos,
            ax=ax,
            with_labels=True,
            node_color="#6a0dad",
            edge_color="#c0a0ff",
        )
    elif type == "entropy-gate":
        G = nx.petersen_graph()
        pos = nx.circular_layout(G)
        nx.draw(
            G,
            pos=pos,
            ax=ax,
            with_labels=True,
            node_color="#0d6a6a",
            edge_color="#a0ffd0",
        )
    ax.set_title(f"{type.capitalize()} Mandala", fontsize=14)
    fig.tight_layout()
    return fig


def climate_dashboard() -> plt.Figure:
    """Render the Climate Entropy Dashboard with fractal waves.

    Returns:
        A :class:`matplotlib.figure.Figure` with the dashboard plot.
    """
    fig, axes = plt.subplots(1, 2, figsize=(12, 5))

    t = np.linspace(0, 10, 300)
    axes[0].plot(t, np.sin(t * 1.618), label="Entropy Wave (φ)", color="#6a0dad")
    axes[0].plot(
        t, np.cos(t * 1.618 / 2), label="Resonance", color="#0d6a6a", linestyle="--"
    )
    axes[0].legend()
    axes[0].set_title("Climate Entropy Dashboard")
    axes[0].set_xlabel("Time")
    axes[0].set_ylabel("Amplitude")

    theta = np.linspace(0, 2 * np.pi, 200)
    r = 1 + 0.5 * np.sin(8 * theta)
    axes[1].plot(r * np.cos(theta), r * np.sin(theta), color="#c0a000")
    axes[1].set_aspect("equal")
    axes[1].set_title("Fractal Mandala Pattern")

    fig.tight_layout()
    return fig


def mermaid_grafana_bridge(data: dict) -> str:  # noqa: ARG001
    """Generate a Mermaid graph string for Grafana integration.

    Args:
        data: Optional data dict (reserved for future use).

    Returns:
        A Mermaid-format graph string.
    """
    return (
        "graph TD\n"
        "  A[Entropy] --> B[Governance]\n"
        "  B --> C[Cosmic Moment]\n"
        "  C --> D[MandalaMap]\n"
        "  D --> A"
    )


def bind_to_utac(beta: float = 0.0625) -> str:
    """Optional binding to utac-core β-Fitting.

    Args:
        beta: The beta fitting parameter.

    Returns:
        Result string from utac-core or an installation hint.
    """
    try:
        from utac_core.core import beta_fit  # type: ignore[import-not-found]

        return str(beta_fit([1.0, 2.0], [0.5, 1.0]))
    except ImportError:
        return (
            f"UTAC binding (beta={beta}) available with"
            " 'pip install mandala-visualizer[stack]'"
        )
