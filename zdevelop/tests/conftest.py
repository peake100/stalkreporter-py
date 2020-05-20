import asyncio
import pytest
import os
from stalkreporter.server import serve


@pytest.fixture(scope="class")
def event_loop():
    """The event loop to use for the test"""
    loop = asyncio.new_event_loop()
    yield loop
    loop.close()


@pytest.fixture(scope="class")
async def service(event_loop: asyncio.AbstractEventLoop,) -> None:
    os.environ["GRPC_HOST"] = "localhost"
    task = event_loop.create_task(serve())
    yield None
    task.cancel()
