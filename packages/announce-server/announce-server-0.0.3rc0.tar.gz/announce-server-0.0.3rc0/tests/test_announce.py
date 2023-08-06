import asyncio
from unittest.mock import AsyncMock, call, patch

import pytest
import socketio

from announce_server.decorator import _announce_server


@pytest.mark.asyncio
async def test_announce_server(event_loop):
    # Mock the socketio.AsyncClient to prevent actual connections

    with patch("announce_server.decorator.sio") as mock_sio:
        # Create a fake sio.connect() function that simulates a retry loop
        async def fake_connect(*args, **kwargs):
            await asyncio.sleep(0.1)
            raise RuntimeError("Failed to connect")

        # Set the fake connect function to be used as a side_effect for the mock
        mock_sio.connect = AsyncMock(side_effect=fake_connect)

        # Define the outer_kwargs for the _announce_server function
        outer_kwargs = {
            "name": "test_server",
            "ip": "127.0.0.1",
            "port": 8000,
            "host_ip": "127.0.0.1",
            "host_port": 5123,
            "retry_interval": 0.001,
        }

        # Run the _announce_server function with a timeout to avoid infinite loop
        try:
            await asyncio.wait_for(_announce_server(**outer_kwargs), timeout=0.105)
        except asyncio.TimeoutError:
            pass

        # Check if sio.connect was called multiple times due to the retry loop
        assert mock_sio.connect.call_count >= 2

        # Check if sio.connect was called with the correct arguments
        mock_sio.connect.assert_has_calls(
            [call("http://127.0.0.1:5123")] * mock_sio.connect.call_count
        )

        # Since we don't have access to the event handlers directly, we can't test them in this way.
        # Instead, you could refactor the code to make the event handlers separate functions that can be tested independently.
