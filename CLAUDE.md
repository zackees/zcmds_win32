# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

`zcmds_win32` ships Unix-style command-line tools (`ls`, `grep`, `tee`, `bash`, `sed`, `awk`, `make`, `dig`, ...) as Python console-script entry points on Windows. Each entry point is a thin Python wrapper that resolves the matching `.exe` from the system, from a local Git for Windows install, or from a bundled/downloaded zip — then `exec`s it with the caller's `sys.argv`.

## Commands

Build / install / test all rely on `uv`. Tests target Python 3.10 on Windows only.

- `pip install -e .` — editable install registers every console script in `pyproject.toml [project.scripts]`.
- `python install.py` — bootstraps a `venv/`, links `venv/bin` to `venv/Scripts` on Windows, runs `pip install -e .`. Must be run from outside an activated venv.
- `. ./activate.sh` — enter the dev venv (creates it if missing).
- `bash lint` — runs `isort --profile black`, `black`, `pylint`, `mypy` against the `zcmds_win32` package (all via `uv run`).
- `uv run pytest tests` — run the full test suite. Single test: `uv run pytest tests/test_main.py::MainTester::test_ls`.
- `tox` — runs flake8 + pylint + mypy + pytest per `tox.ini` (py310 only).
- Releasing — bump `version` in `pyproject.toml` and merge to `main`. `.github/workflows/auto-release.yml` ("Auto Release") publishes to PyPI via Trusted Publishing (environment `pypi`) and creates the `v<version>` tag and GitHub Release. Recovery: run the workflow manually with dry-run unchecked.
- `zcmds_win32 --install` — force re-download of the Git-for-Windows binary bundle into `zcmds_win32/git-bash-bin/`.

## Architecture

### Entry-point dispatch

Every user-facing command is one module under `zcmds_win32/cmds/`, exporting a `main() -> int`, and registered in `pyproject.toml [project.scripts]`. Adding a new command means: (1) create `zcmds_win32/cmds/<name>.py` with `main()`, (2) add a `<name> = "zcmds_win32.cmds.<name>:main"` line to `pyproject.toml`, (3) reinstall with `pip install -e .` so the script wrapper regenerates.

### Three patterns for sourcing the underlying binary

When editing or adding a command, pick the pattern that matches how the tool is delivered:

1. **Git-bash backed tools** (`ls`, `grep`, `sed`, `tee`, `bash`, ...) — call `unix_tool_exec("<name>.exe")` from `zcmds_win32/unix_tool_path.py`. Resolution order: `PATH` (excluding Python `Scripts/` shims, which would re-enter ourselves), then `C:\Program Files\Git\usr\bin`, then `zcmds_win32/git-bash-bin/` (lazily populated by downloading `assets/git-bash-bin.zip` from GitHub raw). The Python-`Scripts` exclusion is load-bearing — without it, calling `ls` would resolve to our own wrapper and recurse.

2. **Standalone bundled tools** (`dig`, ...) — call `get_or_fetch_tool(toolname, tooldir, url)` from `zcmds_win32/install_tool.py`, then `os_exec(path)`. The tool is downloaded once into `zcmds_win32/downloads/<name>/`. See `cmds/dig.py` for the canonical template.

3. **Custom logic** (`home`, `fixvmmem`, `zcmds_win32`, `printenv`) — pure Python. `open` is not provided here; `zcmds` owns it. `fixvmmem` uses `sudo_win32.elevated_exec` to UAC-elevate a `taskkill` of `wslservice.exe`.

### `os_exec` semantics

`zcmds_win32/_exec.py:os_exec` is the single subprocess entry point. By default (`inherit_params=True`) it appends `sys.argv[1:]` to the resolved command so user arguments pass through unchanged. Returns the subprocess exit code — `main()` functions return this directly so console-script wrappers propagate it as the process exit code.

### Assets and downloads

`assets/` holds the source-of-truth zips (`git-bash-bin.zip`, `dig-for-windows-9.9.5-W1.zip`, `make-3.81-bin.zip`). At runtime the code downloads from `https://github.com/zackees/zcmds_win32/raw/main/assets/...` — so committing a new asset and pushing to `main` is what makes it available to installed users. `zcmds_win32/downloads/` and `zcmds_win32/git-bash-bin/` are runtime caches, populated lazily.

## Conventions

- Python 3.10+, formatted with `black` + `isort --profile black`.
- Pylint config in `pyproject.toml` disables `missing-module-docstring` and `missing-function-docstring`; flake8 ignores E501/E203/W503 (`tox.ini`).
- Commands should be tiny — match the existing one-screen pattern. Don't add argument parsing on top of `unix_tool_exec`; the real binary already handles its own flags.
- Bumping the version in `pyproject.toml` on `main` is what triggers a release. Release notes go in `README.md`.
