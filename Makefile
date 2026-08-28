.ONESHELL:
pre-build:
	uv sync --all-extras

build:
	bun install
	bun generate

generate:
	uv run python gfi/populate.py

generate-prod:
	bun install
	bun sync down
	bun generate

test:
	uv run python -m unittest discover gfi
	uv run mypy gfi/*.py

format:
	uv run ruff format .
	bunx prettier --write .

.DEFAULT_GOAL := build
