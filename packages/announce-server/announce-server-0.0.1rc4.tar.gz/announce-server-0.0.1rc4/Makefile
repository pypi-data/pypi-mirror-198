build: clean
	python -m build --sdist --wheel

clean:
	rm -rf dist/ build/ .eggs/ .pytest_cache/ src/announce_server.egg-info/

pub: build
	twine upload dist/*

install:
	pip install -e .[dev,pub]

.PHONY: build clean pub install