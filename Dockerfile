FROM python:3.8-alpine as builder
WORKDIR /
COPY . .
RUN apk update && \
  apk add nodejs curl build-base python3-dev libffi-dev openssl-dev && \
  curl -L -o hugo.tar.gz https://github.com/gohugoio/hugo/releases/download/v0.76.3/hugo_0.76.3_Linux-64bit.tar.gz && \
  tar xzvf hugo.tar.gz && \
  mv hugo /usr/local/bin && \
  pip install --upgrade poetry && \
  ls -al && \
  poetry install --no-dev && \
  poetry run python gfi/populate.py && \
  cd themes/lucy/ && \
  npm install -g postcss postcss-cli postcss-import autoprefixer && \
  hugo

FROM alpine
WORKDIR /
RUN mkdir -p public && \
  mkdir -p resources
COPY --from=builder /public/ public/
COPY --from=builder /resources/ resources/
