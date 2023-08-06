build: clean
	python -m build --sdist --wheel

clean:
	rm -rf dist/ build/ .eggs/ .pytest_cache/ src/announce_server.egg-info/

pub: build
	twine upload dist/*

install:
	pip install -e .[dev,pub]

test-api:
	docker run --rm -ti -p 4999:4999 python:3.7-slim bash -c "pip install -U announce_server~=0.0.2rc0; announce_server start_registry"

.PHONY: build clean pub install test-api