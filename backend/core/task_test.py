import asyncio
from core.task_manager import task_manager


async def demo_task():
    await asyncio.sleep(1)
    return "Task completed successfully"


async def run_test():
    result = await task_manager.run_task(demo_task)

    print("\nTASK RESULT")
    print(result)


if __name__ == "__main__":
    asyncio.run(run_test())
