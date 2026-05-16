import asyncio

async def add(x: int) -> int:
    return x + 1

def main():
    ret = add(1)
    print(f"ret = {ret}")

if __name__ == "__main__":
    main()
