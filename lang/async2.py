import asyncio

async def add(x: int) -> int:
    return x + 1

async def main():
    ret = await add(1)
    print(f"ret = {ret}")

if __name__ == "__main__":
    asyncio.run(main())
