from flet import UserControl, Column, CrossAxisAlignment, MainAxisAlignment
from components.task_item import get_task_item
from json_handler import json_writer


def get_task_list(data):
    task_list = []
    for task in data:
        task_item = get_task_item(task=task["task"], value=task["value"], id=task["id"])
        task_list.append(task_item)
    return task_list


class TaskList(UserControl):
    def __init__(self, data: list[dict]):
        super().__init__()
        self.data = data

    def build(self):
        self.task_list = []
        for task in self.data:
            task_item = get_task_item(
                task=task["task"], value=task["value"], id=task["id"]
            )
            task_item.on_change = self.complete_task
            self.task_list.append(task_item)
        return Column(
            controls=self.task_list,
            horizontal_alignment=CrossAxisAlignment.CENTER,
            alignment=MainAxisAlignment.CENTER,
        )

    def complete_task(self, e):
        new_value = e.control.value
        task_id = e.control.key
        for item in self.data:
            if item["id"] == task_id:
                item["value"] = new_value
                break
        json_writer(self.data)
