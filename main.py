import flet as ft

from components.todo_app import TodoApp
from json_handler import json_reader


def main(page: ft.Page):
    # Configuration
    page.title = "To Do List"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    data = json_reader()

    # Components
    todo_app = TodoApp(data)
    page.add(
        todo_app
    )


if __name__ == "__main__":
    # inicializamos nuestra aplicación
    ft.app(target=main)
