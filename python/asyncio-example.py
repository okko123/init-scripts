import asyncio

## use for create Concurrent connection
TARGET = ("192.168.0.1", 80)

async def tcp_client(i):
    reader, writer = await asyncio.open_connection(*TARGET)

    data = await reader.read(100)
    print(f'No.{i} Received: {data.decode()!r}')

    writer.close()
    await writer.wait_closed()

async def main():
    await asyncio.gather(*(tcp_client(i) for i in range(10)))

asyncio.run(main())
