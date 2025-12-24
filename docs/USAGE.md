# Usage

## Install
- Install locally from the repo root:
  - `pip3 install .`

## Conversion script
- Preferred script: `oasa_convert.py`
- Compatibility wrapper: `convert.py` (prints a deprecation notice)

Examples:
- `python3 oasa_convert.py -c sm -i input.smi -o output.mol`
- `python3 oasa_convert.py -c is -i input.inchi -o output.smi`
- `python3 oasa_convert.py -c ms -i input.mol -o output.smi`

## Smoke rendering test
- Requires `pycairo` in the active environment.
- Renders alpha-d-glucopyranose by default:
  - `python3 tests/smoke_png.py -o output/glucose.png`

## Static checks
- Pyflakes: `tests/run_pyflakes.sh`
- Mypy: `tests/run_mypy.sh`

## Virtual install test
- Creates a temporary venv and installs the repo:
  - `tests/run_virtual_test.sh`
