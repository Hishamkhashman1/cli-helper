from __future__ import annotations

try:
    from .cli import main
except ImportError:  # pragma: no cover - compatibility for direct file execution
    from cli import main


if __name__ == "__main__":
    raise SystemExit(main())
