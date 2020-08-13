THEME_PATH = 'themes/lucy/'

.ONESHELL:
pre-build:
	curl -sSL -o get-poetry.py https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py && \
	python get-poetry.py -y --preview
	export PATH=$$HOME/.poetry/bin:$$PATH
	source $$HOME/.poetry/env
	poetry install --no-dev

.ONESHELL:
build:
	cd $(THEME_PATH) && \
	npm install && \
	cd ../.. & \
	npm install -g postcss-cli autoprefixer postcss-import && \
	hugo -b $$VERCEL_URL

generate:
	poetry run python gfi/populate.py

tweet:
	poetry run python gfi/tweet.py

index:
	poetry run python gfi/index.py

.ONESHELL:
generate-prod:
	make pre-build
	make generate
	@if [ $$PREVIEW == "false" ]; then\
		make tweet; \
	fi; \
	make build

test:
	poetry run python gfi/test_data.py

.DEFAULT_GOAL := build
