THEME_PATH = 'themes/lucy/'

build:
	cd $(THEME_PATH) && \
	npm install && \
	cd ../.. & \
	npm install -g postcss-cli autoprefixer && \
	hugo

generate:
	python populate.py

pre-build:
  curl https://pyenv.run | bash && \
	eval "$(pyenv init -)" && \
	pyenv install 3.8 && \
	pip install --upgrade poetry && \
	poetry config virtualenvs.create false && \
	poetry install && \
	python generate.py

.DEFAULT_GOAL := build

