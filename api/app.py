import asyncio
import celery
import time
import random


# set up celery
celery_app = celery.Celery(
    "celeri",
    backend="redis://redis:6379",
    broker="redis://redis:6379",
)

celery_app.conf.task_routes = {
    "worker.type_a.*": "type_a",
    "worker.type_b.*": "type_b",
}


async def main():
    print("API is running...")

    task_counter = 0

    while True:
        operation = ["type_a", "type_b"][random.randint(0, 1)]
        print(f"[{task_counter}] Sending {operation} operation to worker...")
        celery_app.send_task(f"worker.{operation}.operation", args=[task_counter])
        task_counter += 1

        await asyncio.sleep(random.randint(5, 30))


if __name__ == "__main__":
    asyncio.run(main())
