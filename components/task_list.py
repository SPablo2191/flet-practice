from components.task_item import get_task_item

def get_task_list(data):
    task_list = []
    for task in data:
        task_item = get_task_item(task=task['task'], value= task['value'],id=task['id'])
        task_list.append(
            task_item
        )
    return task_list
