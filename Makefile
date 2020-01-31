THEME_PATH = 'themes/lucy/'

build:
	cd $(THEME_PATH) && \
	npm install && \
	cd ../.. & \
	npm install -g postcss-cli autoprefixer && \
	hugo

.DEFAULT_GOAL := build

