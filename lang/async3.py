import asyncio

async def task_fun(x: int) -> None:
    print(f"start task{x}")
    await asyncio.sleep(x)
    print(f"finish task{x}")


async def main():
    task = asyncio.create_task(task_fun(1))  # <1>
    print(f"task = {task}")
    ret = await task  # <2>
    print(f"ret = {ret}")

if __name__ == "__main__":
    asyncio.run(main())
