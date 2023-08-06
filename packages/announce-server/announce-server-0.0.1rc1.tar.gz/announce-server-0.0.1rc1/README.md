# Announce Server

A Python library that announces a server to a host.

## Installation

```bash
pip install announce-server
```

## Development

To install the developer dependencies required for testing and publishing:
```bash
pip install -e .[dev,pub]
```

## Build
To build the package, run:

```bash
rm -rf dist/ build/ .eggs/ .pytest_cache/ src/announce_server.egg-info/
python -m build --sdist --wheel
```

To publish:
```bash
twine upload dist/*
```

## Test

To run the tests, call:

```bash
pytest
```

## Usage

```python
from announce_server.announce import announce_server

@announce_server(name="server_name", ip="server_ip", port=8000, host_ip="host_server_ip", host_port=5000, retry_interval=5)
def your_function():
    pass

```