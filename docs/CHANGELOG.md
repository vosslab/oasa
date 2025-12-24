# Changelog

## 2025-12-24
- Modernized Python 3 support and packaging (`setup.py`, `README`, `oasa/__init__.py`).
- Added repo documentation for architecture and file layout
  ([docs/CODE_ARCHITECTURE.md](docs/CODE_ARCHITECTURE.md),
  [docs/FILE_STRUCTURE.md](docs/FILE_STRUCTURE.md)).
- Added developer tooling and tests (`tests/`, `mypy.ini`, `pip_requirements.txt`).
- Added smoke rendering test (`tests/smoke_png.py`) that requires `pycairo`.
- Cleaned Pyflakes findings and fixed several runtime issues across core modules.
- Moved legacy conversion logs to [docs/legacy](docs/legacy) and removed generated outputs.
