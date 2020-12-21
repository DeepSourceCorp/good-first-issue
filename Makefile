.ONESHELL:
pre-build:
	pip install --upgrade poetry && \
	poetry install && \
	yarn

build:
	yarn generate

generate:
	poetry run python gfi/populate.py

tweet:
	poetry run python gfi/tweet.py

index:
	poetry run python gfi/index.py

generate-prod:
	make pre-build
	make generate
	@if [ $$PREVIEW == "false" ]; then \
	  make tweet; \
	fi; \
	make build

test:
	poetry run python gfi/test_data.py

.DEFAULT_GOAL := build
