broker_url = "redis://localhost:6379/0"
result_backend = "redis://localhost:6379/0"
accept_content = ["application/json"]
task_serializer = "json"
result_serializer = "json"
enable_utc = True
# task_routes = {
#     'app.tasks.divide_task.divide_task': {'queue': 'divide_task'},
#     'app.tasks.sum_task.sum_task': {'queue': 'sum_task'},
# }