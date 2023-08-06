import argparse
import asyncio
import signal

import socketio
from aiohttp import web

sio = socketio.AsyncServer(async_mode="aiohttp")
app = web.Application()
sio.attach(app)

servers = {}


async def available(request):
    """
    Return a JSON response containing the available servers.

    Returns
    -------
    aiohttp.web.Response
        JSON response containing the available servers.
    """
    return web.json_response(servers)


app.router.add_get("/available", available)


@sio.event
async def connect(sid, environ):
    """Handle a new connection to the socket."""
    print("Connected:", sid)


@sio.event
async def register(sid, data):
    """
    Register a new server.

    Parameters
    ----------
    sid : str
        Socket ID of the connected server.
    data : dict
        Server information (name, IP, and port).
    """
    server_info = data
    name = server_info["name"]

    servers[name] = {"ip": server_info["ip"], "port": server_info["port"], "sid": sid}
    print(servers)


@sio.event
async def disconnect(sid):
    """
    Handle a server disconnect.

    Parameters
    ----------
    sid : str
        Socket ID of the disconnected server.
    """
    print("Disconnected from server:", sid)
    for name, server in servers.items():
        if server["sid"] == sid:
            del servers[name]
            break


async def heartbeat(sio, interval, timeout):
    """
    Periodically send heartbeat messages to connected servers.

    Parameters
    ----------
    sio : socketio.AsyncServer
        The socket.io server instance.
    interval : int
        The interval between heartbeat messages in seconds.
    timeout : int
        The timeout for waiting for a response in seconds.
    """
    while True:
        await asyncio.sleep(interval)
        server_values_copy = list(servers.values())
        for server in server_values_copy:
            sid = server["sid"]
            try:
                print(f"Sending heartbeat to {sid}...")
                heartbeat_future = sio.emit("heartbeat", to=sid)
                await asyncio.wait_for(heartbeat_future, timeout=timeout)
            except (asyncio.TimeoutError, socketio.exceptions.TimeoutError):
                print(f"Server {sid} failed to respond to heartbeat after {timeout}s.")
                await sio.disconnect(sid)


def create_exit_handler(loop, heartbeat_task):
    """
    Create an exit handler for gracefully shutting down the server.

    Parameters
    ----------
    loop : asyncio.AbstractEventLoop
        The event loop.
    heartbeat_task : asyncio.Task
        The heartbeat task.

    Returns
    -------
    Callable
        An asynchronous exit handler function.
    """

    async def exit_handler(sig, frame):
        print("Shutting down host...")
        heartbeat_task.cancel()
        await loop.shutdown_asyncgens()
        loop.stop()

    return exit_handler


def start_server(address, port, heartbeat_interval, heartbeat_timeout):
    """
    Run the main server loop.

    Parameters
    ----------
    address : str
        The IP address of the server.
    port : int
        The port number of the server.
    heartbeat_interval : int
        The interval between heartbeat messages in seconds.
    heartbeat_timeout : int
        The timeout for waiting for a response in seconds.
    """
    loop = asyncio.get_event_loop()
    # Python 3.7+, coroutines only:
    # heartbeat_task = loop.create_task(
    #     heartbeat(sio, heartbeat_interval, heartbeat_timeout)
    # )
    # aiohttp_app = loop.create_task(web._run_app(app, host=address, port=port))

    # Python 3.6+ compatible. Supports any awaitable:
    heartbeat_task = asyncio.ensure_future(
        heartbeat(sio, heartbeat_interval, heartbeat_timeout)
    )

    aiohttp_app = asyncio.ensure_future(web._run_app(app, host=address, port=port))

    exit_handler = create_exit_handler(loop, heartbeat_task)
    signal.signal(signal.SIGINT, exit_handler)
    signal.signal(signal.SIGTERM, exit_handler)

    try:
        loop.run_until_complete(asyncio.gather(heartbeat_task, aiohttp_app))
    except asyncio.CancelledError:
        pass
    finally:
        loop.run_until_complete(loop.shutdown_asyncgens())
        loop.stop()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Start announce_server client.")

    parser.add_argument("--ip", default="0.0.0.0", help="IP address of the host server")
    parser.add_argument(
        "--port", default=4999, type=int, help="Port of the host server"
    )
    parser.add_argument(
        "--heartbeat-interval",
        default=5,
        type=float,
        help="Heartbeat interval in seconds",
    )
    parser.add_argument(
        "--heartbeat-timeout",
        default=3,
        type=float,
        help="Heartbeat timeout in seconds",
    )

    args = parser.parse_args()

    start_server(
        address=args.ip,
        port=args.port,
        heartbeat_interval=args.heartbeat_interval,
        heartbeat_timeout=args.heartbeat_timeout,
    )
