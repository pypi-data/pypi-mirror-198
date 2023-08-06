import asyncio
from functools import wraps

import socketio

sio = socketio.AsyncClient()


async def _announce_server(**kwargs):
    SERVER_NAME = kwargs.get("name", "server_1")
    SERVER_IP = kwargs.get("ip", "localhost")
    SERVER_PORT = kwargs.get("port", 8000)
    HOST_SERVER_IP = kwargs.get("host_ip", "0.0.0.0")
    HOST_SERVER_PORT = kwargs.get("host_port", 5000)
    RETRY_INTERVAL = kwargs.get("retry_interval", 5)

    @sio.event
    async def connect():
        await sio.emit(
            "register", {"name": SERVER_NAME, "ip": SERVER_IP, "port": SERVER_PORT}
        )
        print("Announced server to host")

    async def main():
        # retry until we connect to the host
        while True:
            try:
                await sio.connect(f"http://{HOST_SERVER_IP}:{HOST_SERVER_PORT}")
                break
            except Exception as e:
                print(e)
                print("Failed to connect to host, retrying in 5 seconds")
                await asyncio.sleep(RETRY_INTERVAL)
        # await sio.connect(f'http://{HOST_SERVER_IP}:{HOST_SERVER_PORT}')
        print("Connected to host")

    @sio.on("heartbeat")
    async def on_heartbeat():
        print("Received heartbeat from host")

    @sio.event
    async def disconnect():
        print("Disconnected from host")

    await main()


def announce_server(task=None, **outer_kwargs):
    if task is None:
        return lambda f: announce_server(f, **outer_kwargs)

    @wraps(task)
    def wrapper(*args, **kwargs):
        async def main(*args, **kwargs):
            loop = asyncio.get_event_loop()
            host_block_thread = loop.run_in_executor(None, task)

            # Announce the server to the host
            await _announce_server(**outer_kwargs)

            # Wait for host_block to finish
            await host_block_thread

        return asyncio.run(main())

    return wrapper
