# claudebasics

A Python project for exploring Claude API / agentic AI basics.

## Environment

- Python 3.13 (CPython)
- Virtual environment managed by `uv`, located at `.venv/`
- Activate (bash): `source .venv/Scripts/activate`
- Activate (PowerShell): `.venv\Scripts\Activate.ps1`

## Common commands

- Install deps: `uv pip install -r requirements.txt`
- Add a dep: append to `requirements.txt`, then re-run install
- Run REPL: `python main.py` — prompts `> `, supports `+ - * /`, type `quit` or `exit` to leave (Ctrl+D / Ctrl+Z also exit)
- Run tests: `uv run pytest`

## Layout

- `main.py` — interactive calculator REPL (entry point)
- `calculator.py` — pure arithmetic functions: `add`, `subtract`, `multiply`, `divide`
- `tests/` — pytest test suite
- `conftest.py` — empty marker so pytest treats the project root as rootdir (puts root on `sys.path`)
- `requirements.txt` — pinned dependencies

## Conventions

- Use `uv` (not bare `pip`) for all package operations.
- Keep `requirements.txt` as the single source of truth for dependencies.
- Keep arithmetic logic in `calculator.py` as pure functions; `main.py` should stay a thin I/O layer over it.

## Maintaining this file

Update this file as the project grows: new commands, new top-level files/folders, new conventions, or gotchas worth remembering between sessions. Keep entries concrete and scoped to this repo — generic Python advice doesn't belong here.
