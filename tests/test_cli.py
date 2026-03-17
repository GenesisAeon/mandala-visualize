"""Tests for the mviz CLI commands."""

from pathlib import Path

import pytest
from typer.testing import CliRunner

from mandala_visualizer.cli import app

runner = CliRunner()


def test_render_cosmic_web(tmp_path):
    result = runner.invoke(app, ["render", "--type", "cosmic-web", "--output", str(tmp_path / "out.png")])
    assert result.exit_code == 0, result.output
    assert (tmp_path / "out.png").exists()


def test_render_entropy_gate(tmp_path):
    result = runner.invoke(app, ["render", "--type", "entropy-gate", "--output", str(tmp_path / "eg.png")])
    assert result.exit_code == 0, result.output
    assert (tmp_path / "eg.png").exists()


def test_dashboard(tmp_path):
    result = runner.invoke(app, ["dashboard", "--output", str(tmp_path / "dash.png")])
    assert result.exit_code == 0, result.output
    assert (tmp_path / "dash.png").exists()


def test_bridge():
    result = runner.invoke(app, ["bridge"])
    assert result.exit_code == 0, result.output
    assert "Entropy" in result.output
    assert "Governance" in result.output
