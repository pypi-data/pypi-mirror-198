from typing import Callable


class HelloRequest:
    name: str
    def __new__(cls, name: str) -> HelloRequest: ...


class HelloResponse:
    message: str
    def __new__(cls, message: str) -> HelloResponse: ...


async def serve_greeter(
    hello: Callable[[HelloRequest], HelloResponse], port=50051): ...
