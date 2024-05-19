from flet import (
    UserControl,
    TextField,
    IconButton,
    icons,
    Text,
    FontWeight,
    Column,
    Row,
    MainAxisAlignment,
    CrossAxisAlignment,
)

from components.task_item import get_task_item
from json_handler import json_writer


class TodoApp(UserControl):
    def __init__(self, data: list[dict]):
        super().__init__()
        self.data = data

    def build(self):
        self.main_title = Text(value="To Do List", size=30, weight=FontWeight.BOLD)
        self.txt_input = TextField(
            hint_text="Ingrese un tarea por hacer...", expand=True
        )
        self.btn_add = IconButton(icon=icons.ADD_ROUNDED, on_click=self.add_task)
        self.tasks = self.load_task()
        return Column(
            controls=[
                self.main_title,
                Row(
                    controls=[self.txt_input, self.btn_add],
                    alignment=MainAxisAlignment.CENTER,
                ),
                self.tasks,
            ],
            horizontal_alignment=CrossAxisAlignment.CENTER,
        )

    def load_task(self):
        task_list = []
        for task in self.data:
            task_item = get_task_item(
                task=task["task"], value=task["value"], id=task["id"]
            )
            task_item.on_change = self.complete_task
            task_list.append(task_item)
        return Column(
            controls=task_list,
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

    def add_task(self, e):
        # get task
        new_task = self.txt_input.value
        self.txt_input.value = ""

        # write task in json
        new_task_data = {"task": new_task, "value": False, "id": len(self.data) + 1}
        self.data.append(new_task_data)
        json_writer(self.data)

        # add task in Column
        self.tasks.controls.append(
            get_task_item(
                task=new_task_data["task"],
                value=new_task_data["value"],
                id=new_task_data["id"],
            )
        )
        self.update()
