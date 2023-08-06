from unittest.mock import MagicMock, patch

import pytest

from announce_server.decorator import (
    announce_server,
    register_block,
    register_server,
    register_service,
)


@pytest.mark.parametrize(
    "decorator_alias",
    [
        register_block,
        register_server,
    ],
)
def test_alias_calls_register_service(decorator_alias):
    test_args = (None, None)
    test_kwargs = {
        "name": "test_server",
        "ip": "127.0.0.1",
        "port": 8000,
        "host_ip": "127.0.0.1",
        "host_port": 5000,
    }

    with patch("announce_server.decorator.register_service") as mock_register_service:
        mock_register_service.return_value = MagicMock()

        decorator = decorator_alias(*test_args, **test_kwargs)
        decorator(MagicMock())

        mock_register_service.assert_called_once_with(*test_args, **test_kwargs)


@pytest.mark.parametrize(
    "decorator_alias",
    [
        announce_server,
    ],
)
def test_deprecated_alias_calls_register_service(decorator_alias):
    test_args = (None, None)
    test_kwargs = {
        "name": "test_server",
        "ip": "127.0.0.1",
        "port": 8000,
        "host_ip": "127.0.0.1",
        "host_port": 5000,
    }
    with patch("announce_server.decorator.register_service") as mock_register_service:
        mock_register_service.return_value = MagicMock()

        with pytest.warns(DeprecationWarning):
            decorator = decorator_alias(*test_args, **test_kwargs)

        decorator(MagicMock())
        mock_register_service.assert_called_once_with(*test_args, **test_kwargs)
