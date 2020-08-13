THEME_PATH = 'themes/lucy/'

pre-build:
	pip install --user --pre poetry -U && \
	export PATH=$$HOME/.poetry/bin:$$PATH && \
	poetry self update --preview && \
	poetry install --no-dev

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
