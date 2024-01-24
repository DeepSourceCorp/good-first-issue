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
	bun install
	bun sync down
	bun generate

test:
	poetry run python gfi/test_data.py
	poetry run mypy gfi/*.py

format:
	poetry run ruff format .
	bunx prettier --write .

.DEFAULT_GOAL := build

first-run:
	cp data/generated.sample.json data/generated.json
	cp data/tags.sample.json data/tags.json
	cp static/sw.sample.js static/sw.js
	yarn
	yarn dev -o
