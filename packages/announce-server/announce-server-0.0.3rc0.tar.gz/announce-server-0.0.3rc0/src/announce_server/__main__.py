import argparse

from announce_server import register_service
from announce_server.client import start_client
from announce_server.server import start_server


def main():
    parser = argparse.ArgumentParser(description="Announce server CLI")
    subparsers = parser.add_subparsers(dest="command", help="Available subcommands")

    # Start registry subcommand
    start_registry_parser = subparsers.add_parser(
        "start_registry", help="Start the registry server"
    )
    start_registry_parser.add_argument(
        "--ip", default="0.0.0.0", help="IP address of the host server"
    )
    start_registry_parser.add_argument(
        "--port", default=4999, type=int, help="Port of the host server"
    )
    start_registry_parser.add_argument(
        "--heartbeat-interval",
        default=5,
        type=float,
        help="Heartbeat interval in seconds",
    )
    start_registry_parser.add_argument(
        "--heartbeat-timeout",
        default=3,
        type=float,
        help="Heartbeat timeout in seconds",
    )

    # Start client subcommand
    start_client_parser = subparsers.add_parser(
        "start_client", help="Start the client server"
    )
    start_client_parser.add_argument(
        "--host-ip",
        type=str,
        default="0.0.0.0",
        help="Host IP address (default: 0.0.0.0)",
    )
    start_client_parser.add_argument(
        "--host-port", type=int, default=4999, help="Host port number (default: 4999)"
    )

    args = parser.parse_args()

    if args.command == "start_registry":
        start_server(
            address=args.ip,
            port=args.port,
            heartbeat_interval=args.heartbeat_interval,
            heartbeat_timeout=args.heartbeat_timeout,
        )
    elif args.command == "start_client":
        start_client(host_ip=args.host_ip, host_port=args.host_port)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
