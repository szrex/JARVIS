import asyncio
import uuid
from datetime import datetime, timezone


class TaskManager:

    def __init__(self):
        self.tasks = {}

    async def run_task(self, task_function, *args, **kwargs):
        task_id = str(uuid.uuid4())

        self.tasks[task_id] = {
            "id": task_id,
            "status": "running",
            "started_at": datetime.now(timezone.utc).isoformat()
        }

        try:
            result = await task_function(*args, **kwargs)

            self.tasks[task_id].update({
                "status": "completed",
                "result": result,
                "completed_at": datetime.now(timezone.utc).isoformat()
            })

        except Exception as error:
            self.tasks[task_id].update({
                "status": "failed",
                "error": str(error),
                "completed_at": datetime.now(timezone.utc).isoformat()
            })

        return self.tasks[task_id]

    def get_task(self, task_id):
        return self.tasks.get(task_id)

    def get_all_tasks(self):
        return list(self.tasks.values())


task_manager = TaskManager()
