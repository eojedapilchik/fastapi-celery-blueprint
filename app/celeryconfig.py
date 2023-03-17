broker_url = "redis://localhost:6379/0"
result_backend = "redis://localhost:6379/0"
accept_content = ["application/json"]
task_serializer = "json"
result_serializer = "json"
enable_utc = True
worker_send_task_events = True
task_create_missing_queues = True
# Add the task routes
task_routes = {
    "app.tasks.sum_task.sum_task": {"queue": "sum_queue"},
    "app.tasks.divide_task.divide_task": {"queue": "divide_queue"},
}