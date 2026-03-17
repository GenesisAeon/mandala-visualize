"""Tests for mandala_visualizer.core."""

import matplotlib
import matplotlib.pyplot as plt

matplotlib.use("Agg")  # non-interactive backend for tests

from mandala_visualizer.core import (
    bind_to_utac,
    climate_dashboard,
    mermaid_grafana_bridge,
    render_mandala,
)


def test_render_mandala_cosmic_web():
    fig = render_mandala("cosmic-web")
    assert isinstance(fig, plt.Figure)
    plt.close(fig)


def test_render_mandala_entropy_gate():
    fig = render_mandala("entropy-gate")
    assert isinstance(fig, plt.Figure)
    plt.close(fig)


def test_render_mandala_default():
    fig = render_mandala()
    assert isinstance(fig, plt.Figure)
    plt.close(fig)


def test_climate_dashboard():
    fig = climate_dashboard()
    assert isinstance(fig, plt.Figure)
    assert len(fig.axes) == 2
    plt.close(fig)


def test_mermaid_grafana_bridge():
    result = mermaid_grafana_bridge({})
    assert "graph TD" in result
    assert "Entropy" in result
    assert "Governance" in result
    assert "Cosmic Moment" in result
    assert "MandalaMap" in result


def test_mermaid_grafana_bridge_with_data():
    result = mermaid_grafana_bridge({"key": "value"})
    assert isinstance(result, str)


def test_bind_to_utac_no_stack():
    """Without utac-core installed, bind_to_utac returns an installation hint."""
    result = bind_to_utac()
    assert isinstance(result, str)


def test_bind_to_utac_custom_beta():
    result = bind_to_utac(beta=0.125)
    assert isinstance(result, str)
