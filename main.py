import flet as ft

from components.task_item import get_task_item
from components.task_list import get_task_list
from json_handler import json_reader, json_writer


def main(page: ft.Page):
    """ Función main
    es nuestra función "objetivo" en la cual definiremos todo lo que conformara la aplicación al ejecutarse.
    """


    """ Configuración
    En esta primera parte definimos aspectos de nuestra page (todo nuestro lienzo en el que "dibujaremos" nuestros controles)
    Aqui definimos cosas tan simples como el nombre que tendra nuestro programa al ejecutarse, como el tema o la fuente que
    queramos utilizar.
    """
    page.title = "To Do List"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    data = json_reader()

    """ Funciones Eventos
    Aqui definiremos que funciones que se ejecuten cuando se desencadene un evento en especifico.
    add_task, por ejemplo,cuando ocurra algun evento y esta este asociada a ese; añadira una task a la lista
    y al mismo tiempo la añadira al archivo json.
    """
    def add_task(e):
        # obtener la información del espacio de texto
        new_task = txt_input.value
        txt_input.value = ""
        txt_input.update()

        # escribimos la tarea en el json
        new_task_data = {"task": new_task, "value": False, "id": len(data) + 1}
        data.append(new_task_data)
        json_writer(data)

        # añadimos la tarea en el json
        tasks.controls.append(
            get_task_item(
                task=new_task_data["task"],
                value=new_task_data["value"],
                id=new_task_data["id"],
            )
        )
        tasks.update()
        
    def complete_task(e):
        # obtenemos el checkbox seleccionado
        new_value = e.control.value
        task_id = e.control.key
        # lo buscamos en nuestra "base de datos"
        for item in data:
            if item['id'] == task_id:
                item['value'] = new_value
                break
        # lo añadimos al json
        json_writer(data)
    
    """ componentes / controles / widgets
    aqui definimos y almacenamos en variables los distintos controles que podemos llegar a utilizar.
    """
    txt_input = ft.TextField(hint_text="Ingrese un tarea por hacer...", expand=True)
    btn_add = ft.IconButton(icon=ft.icons.ADD_ROUNDED, on_click=add_task)
    main_title = ft.Text(value="To Do List", size=30, weight=ft.FontWeight.BOLD)

    # le asignamos a cada checkbox la funcion a ejecutar cuando ocurra un evento "on_change"
    task_list = get_task_list(data)
    for task_item in task_list:
        task_item.on_change = complete_task

    # creamos la lista de checkboxes
    tasks = ft.Column(
        controls=task_list,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        alignment=ft.MainAxisAlignment.CENTER,
    )
    """Montaje
    Aqui añadimos o montamos los componentes creados en nuestra aplicación formalmente.
    """
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
