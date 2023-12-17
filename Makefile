.ONESHELL:
pre-build:
	pip install --upgrade poetry
	poetry install --no-root

build:
	bun install
	bun generate

generate:
	poetry run python gfi/populate.py

generate-prod:
	make pre-build
	make generate
	make build

test:
	poetry run python gfi/test_data.py
	poetry run mypy gfi/*.py

format:
	poetry run ruff format .
	bunx prettier --write .

.DEFAULT_GOAL := build
