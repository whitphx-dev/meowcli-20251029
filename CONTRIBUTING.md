# Contributing

Thanks for your interest!

## Workflow
1. Pick or open an Issue
2. Fork & create a branch
3. Make a small change and open a Draft PR
4. CI turns green -> Ready for review

## Local dev

First, install `uv` (see [official docs](https://docs.astral.sh/uv/getting-started/installation/)):
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Then set up the project:
```bash
uv sync
```

### Running tests

```bash
uv run pytest
```

### Code style (Ruff)

Use Ruff for formatting and linting:

```bash
# Format code
uv run ruff format .

# Lint and auto-fix simple issues
uv run ruff check . --fix
```
