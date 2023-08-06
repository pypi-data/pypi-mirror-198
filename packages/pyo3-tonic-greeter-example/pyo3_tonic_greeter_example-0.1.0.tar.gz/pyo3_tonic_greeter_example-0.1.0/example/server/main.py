from pyo3_tonic_greeter_example import serve_greeter, HelloRequest, HelloResponse
import asyncio


def hello(request: HelloRequest) -> HelloResponse:
    return HelloResponse(f'Hello {request.name}!')


async def main():
    await serve_greeter(hello)

asyncio.run(main())
