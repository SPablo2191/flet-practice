from flet import Checkbox


def get_task_item(task: str, value: bool = False, id: int = 0):
    return Checkbox(label=task, value=value, key=id)
