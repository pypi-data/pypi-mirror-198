import asyncio
import subprocess
from unittest.mock import MagicMock, patch

import pytest

from announce_server.decorator import _announce_server, announce_server


@patch("announce_server.decorator._announce_server")
def test_announce_server_decorator(mock_announce_server):
    # Mock the _announce_server function to prevent actual connections
    mock_announce_server.return_value = MagicMock()

    # Decorate the sample function with announce_server
    @announce_server(
        name="test_server",
        ip="127.0.0.1",
        port=8000,
        host_ip="127.0.0.1",
        host_port=5000,
    )
    def http_server():
        server = subprocess.Popen(["python3", "-m", "http.server", "13373"])
        yield
        server.terminate()
        server.wait()

    # Run the decorated function
    http_server()

    # Check if the _announce_server function was called with the correct arguments
    mock_announce_server.assert_called_once_with(
        name="test_server",
        ip="127.0.0.1",
        port=8000,
        host_ip="127.0.0.1",
        host_port=5000,
    )
