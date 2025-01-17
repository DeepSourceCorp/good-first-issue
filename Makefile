# The .ONESHELL directive allows all lines in a recipe to be executed in a single shell instance.
.ONESHELL:

# The 'pre-build' target sets up the project dependencies using Poetry, a Python dependency manager.
pre-build:
	pip install --upgrade poetry  # Updates Poetry to the latest version.
	poetry install --no-root     # Installs project dependencies without installing the project itself.

# The 'build' target installs dependencies and generates necessary resources for the project.
build:
	bun install          # Installs dependencies using Bun, a JavaScript package manager.
	bun generate         # Runs the generation process for the project.

# The 'generate' target runs a Python script to populate project-specific data.
generate:
	poetry run python gfi/populate.py  # Executes the populate.py script to generate data.

# The 'generate-prod' target prepares production-ready resources by syncing and generating required files.
generate-prod:
	bun install          # Installs dependencies using Bun.
	bun sync down        # Synchronizes necessary files or data, such as downloading remote assets.
	bun generate         # Generates required resources for production.

# The 'test' target runs tests and performs type-checking to ensure code quality.
test:
	poetry run python gfi/test_data.py  # Executes a test script for verifying data integrity.
	poetry run mypy gfi/*.py            # Runs static type checks on Python files in the gfi directory.

# The 'format' target ensures consistent code formatting across the project.
format:
	poetry run ruff format .            # Formats Python files using Ruff.
	bunx prettier --write .             # Formats JavaScript, CSS, or other files using Prettier.

# The default goal is set to 'build', meaning this target is executed if no target is specified when running 'make'.
.DEFAULT_GOAL := build
