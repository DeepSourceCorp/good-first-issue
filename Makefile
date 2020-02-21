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
	poetry run python gfi/populate.py

index:
	poetry run python gfi/index.py

generate-prod:
	make pre-build
	make generate
	make build

test:
	poetry run python gfi/test_data.py

.DEFAULT_GOAL := build
