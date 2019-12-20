.PHONY: build run all

all: build run

build:
	docker build -t ml1 \
		--build-arg UID=$(shell id -u) \
		./docker-build-assets

run:
	docker run \
		-it \
		-v $(shell pwd)/src:/home/ml1/src \
		-w /home/ml1/src \
		 --name ml1 --rm ml1 bash