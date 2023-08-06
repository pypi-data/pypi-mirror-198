import asyncio
import socket
from concurrent.futures import ThreadPoolExecutor
from unittest.mock import MagicMock, patch

import pytest

from announce_server import get_ip_address


@pytest.mark.asyncio
async def test_get_ip_address():
    with patch("socket.socket") as mock_socket:
        # Create a MagicMock object for the socket object
        mock_socket_instance = MagicMock()
        mock_socket.return_value = mock_socket_instance

        # Define the expected IP address
        expected_ip = "192.168.1.100"

        # Configure the mock socket instance to return the expected IP address
        mock_socket_instance.getsockname.return_value = (expected_ip, 0)

        # Test the get_ip_address function
        # result_ip = await asyncio.to_thread(get_ip_address)
        # loop = asyncio.get_event_loop()
        # with ThreadPoolExecutor() as pool:
        #     result_ip = await loop.run_in_executor(pool, get_ip_address)

        result_ip = get_ip_address()

        # Check if the result matches the expected IP address
        assert result_ip == expected_ip

        # Check if the socket object was created with the correct arguments
        mock_socket.assert_called_once_with(socket.AF_INET, socket.SOCK_DGRAM)

        # Check if the socket.connect method was called with the correct arguments
        mock_socket_instance.connect.assert_called_once_with(("10.255.255.255", 1))

        # Check if the socket.close method was called
        mock_socket_instance.close.assert_called_once()
