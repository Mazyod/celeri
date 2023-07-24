import asyncio
import celery
import random
import time

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


@celery_app.task(name="worker.type_a.operation")
def type_a_operation(index: int, **kwargs):
    print(f">>> RUNNING: [{index}] type_a")
    time.sleep(random.randint(45, 90))


@celery_app.task(name="worker.type_b.operation")
def type_b_operation(index, **kwargs):
    print(f">>> RUNNING: [{index}] type_b")
    time.sleep(random.randint(45, 90))
