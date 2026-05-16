import asyncio  # <1>

async def add(x: int) -> int:
    return x + 1

async def main():  # <2>
    ret = await add(1)      # <3>
    print(f"ret = {ret}")

if __name__ == "__main__":
    asyncio.run(main())  # <4>
