THEME_PATH = 'themes/lucy/'

pre-build:
	pip install --upgrade poetry && \
	poetry install --no-dev

build:
	cd $(THEME_PATH) && \
	npm install && \
	cd ../.. & \
	npm install -g postcss-cli autoprefixer && \
	hugo

generate:
	poetry run python populate.py

generate-prod:
	make pre-build
	make generate
	make build

.DEFAULT_GOAL := build
