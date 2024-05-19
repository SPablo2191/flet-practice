import flet as ft

from components.task_item import get_task_item
from components.task_list import get_task_list
from json_handler import json_reader, json_writer


def main(page: ft.Page):
    # Configuration
    page.title = "To Do List"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    data = json_reader()

    # Events
    def add_task(e):
        # get task
        new_task = txt_input.value
        txt_input.value = ""
        txt_input.update()

        # write task in json
        new_task_data = {"task": new_task, "value": False, "id": len(data) + 1}
        data.append(new_task_data)
        json_writer(data)

        # add task in Column
        tasks.controls.append(
            get_task_item(
                task=new_task_data["task"],
                value=new_task_data["value"],
                id=new_task_data["id"],
            )
        )
        tasks.update()
        
    def complete_task(e):
        new_value = e.control.value
        task_id = e.control.key
        for item in data:
            if item['id'] == task_id:
                item['value'] = new_value
                break
        json_writer(data)
    
    # Components
    txt_input = ft.TextField(hint_text="Ingrese un tarea por hacer...", expand=True)
    btn_add = ft.IconButton(icon=ft.icons.ADD_ROUNDED, on_click=add_task)
    main_title = ft.Text(value="To Do List", size=30, weight=ft.FontWeight.BOLD)
    task_list = get_task_list(data)
    for task_item in task_list:
        task_item.on_change = complete_task

    # Data
    tasks = ft.Column(
        controls=task_list,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        alignment=ft.MainAxisAlignment.CENTER,
    )
    page.add(
        ft.Column(
            controls=[
                main_title,
                ft.Row(
                    controls=[txt_input, btn_add],
                    alignment=ft.MainAxisAlignment.CENTER,
                ),
                tasks,
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )
    )


if __name__ == "__main__":
    # inicializamos nuestra aplicación
    ft.app(target=main)
