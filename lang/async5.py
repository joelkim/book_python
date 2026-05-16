import asyncio

async def task_fun(x: int) -> None:
    print(f"start task{x}")
    await asyncio.sleep(x)
    print(f"finish task{x}")

async def main():

    task3 = asyncio.create_task(task_fun(3))
    task2 = asyncio.create_task(task_fun(2))
    task1 = asyncio.create_task(task_fun(1))

    ret = await task3

if __name__ == "__main__":
    asyncio.run(main())
