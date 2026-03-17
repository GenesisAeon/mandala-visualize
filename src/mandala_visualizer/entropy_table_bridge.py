"""Bridge to entropy-table for domain relation tracking."""

from __future__ import annotations

from pathlib import Path


class MandalaVisualizerBridge:
    """Bridge between mandala-visualizer and entropy-table.

    Requires ``pip install mandala-visualizer[stack]`` for full functionality.
    """

    def __init__(self) -> None:
        try:
            from entropy_table import EntropyTable  # type: ignore[import-not-found]

            self.table = EntropyTable(domain="mandala-visualizer")
            self._available = True
        except ImportError:
            self.table = None
            self._available = False

    def add_visual(self, key: str, value: str) -> None:
        """Add a visual relation to the entropy table."""
        if not self._available or self.table is None:
            raise RuntimeError("entropy-table not installed. Run: pip install mandala-visualizer[stack]")
        self.table.add_relation(key, value)

    def export(self, filepath: Path | str = "domains.yaml") -> Path:
        """Export the entropy table to a YAML file."""
        if not self._available or self.table is None:
            raise RuntimeError("entropy-table not installed. Run: pip install mandala-visualizer[stack]")
        self.table.export(filepath)
        return Path(filepath)

    @property
    def available(self) -> bool:
        """True if entropy-table is installed and the bridge is functional."""
        return self._available
