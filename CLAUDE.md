# CLAUDE.md

Guidance for AI agents (and humans) working in the **template-python-uv** repo.

## What template-python-uv is

Python package template: uv, pytest, ruff, PyPI trusted publishing, mise, lefthook, CI and a VitePress docs site. A Python package in a `src/` layout, built with `uv_build`, managed entirely with uv, tested with pytest, linted and formatted with ruff.

## Commands

`mise trust && mise install` once per clone, then `mise run install` (= `uv sync --locked`). **All Python goes through uv**: uv owns the interpreter (`.python-version`, `requires-python`) and the venv; mise only pins uv itself. Never use `pip`, `python -m venv` or `poetry`. `mise` puts `.venv/bin` on PATH and loads `.env`, so run tools bare (`pytest`, `ruff`), not `uv run pytest`.

- `mise run check`: `ruff format --check .` + `ruff check .`. **Must be clean before committing.** `mise run fmt` fixes.
- `mise run test`: `pytest`. **Must be green before committing.**
- `mise run build`: `uv build` (sdist + wheel in `dist/`).
- Add a dependency with `uv add <pkg>` (or `uv add --dev <pkg>`); commit `uv.lock`.

CI runs the same mise tasks.

## Architecture

- `src/template_python_uv/`: the package. `__init__.py` is the public API; `cli.py` is the `template-python-uv` console script (thin).
- `tests/`: pytest, importing the installed package (editable via uv).
- `pyproject.toml` holds metadata, the build backend, pytest and ruff config. The `uv_build` module name must match the directory under `src/`.

## Conventions that bite

- CI installs with `--locked`: after changing dependencies, commit the updated `uv.lock` or CI fails.
- `uv_build` is pinned `>=0.12.22,<0.13` to match the uv in `mise.toml`; bump them together.
- ruff is the only formatter and linter (`E F I UP B SIM RUF`).

## Things that bit us

- (none yet)

## Releasing

Bump `version` in `pyproject.toml`, update CHANGELOG, merge, then `git tag vX.Y.Z && git push origin vX.Y.Z`. `release.yml` verifies tag == version, re-runs the gates and publishes to PyPI via trusted publishing (setup notes at the top of the workflow). A manual run publishes to TestPyPI. Don't tag or publish unless asked.

## Changelog

`CHANGELOG.md` follows [Keep a Changelog](https://keepachangelog.com). Every user-facing change adds a bullet under `## [Unreleased]` in the same change as the code.

## Git workflow

- Branch off `main`. Conventional commits (lefthook `commit-msg`). PRs are draft by default.
- **Worktrees go in `.claude/worktrees/<branch-with-dashes>` inside this repo.** Never under `/tmp` or a scratchpad, and never create venvs or install there. Remove after merge.
- Dependabot patch/minor PRs auto-merge on green; major bumps need a human.

## Docs site

`docs/` is a VitePress site and its own pnpm root (`cd docs && pnpm install && pnpm dev`; build with `pnpm build`). `.github/workflows/docs.yml` deploys it to GitHub Pages on pushes to `main` that touch `docs/`. The base path is `/template-python-uv/`; set `DOCS_BASE=/` when it moves to a custom domain. A dead link fails the build, so link repo files via github.com URLs.
