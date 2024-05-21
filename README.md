# Taller de desarrollo de interfaces graficas con Flet🚀
¡Bienvenido al Taller de Desarrollo de Interfaces Gráficas con Flet! En este taller, aprenderemos a utilizar el paquete de Python "flet" para crear aplicaciones de interfaz gráfica de usuario (GUI). Además, veremos cómo configurar entornos virtuales con `venv` tanto en Windows como en Linux para mantener nuestros proyectos organizados y manejables.

## Contenidos

- [Requisitos](#requisitos)
- [Instalación de Flet](#instalación-de-flet)
- [Configuración de Entornos Virtuales](#configuración-de-entornos-virtuales)
  - [Windows](#windows)
  - [Linux](#linux)
- [Primer Proyecto con Flet](#primer-proyecto-con-flet)
- [Recursos Adicionales](#recursos-adicionales)

## Requisitos

Antes de comenzar, asegúrate de tener instalado lo siguiente:

- Python 3.7 o superior
- pip (gestor de paquetes de Python)

## Instalación de Flet

Para instalar el paquete de Flet, ejecuta el siguiente comando en tu terminal:

```sh
pip install flet
```

## Configuración de Entornos Virtuales

La configuración de un entorno virtual es esencial para mantener tus dependencias organizadas y evitar conflictos entre proyectos. A continuación, se detallan los pasos para crear un entorno virtual en Windows y Linux.

### Windows

1. **Crear un entorno virtual:**

   Abre una terminal (CMD, PowerShell o Git Bash) y navega hasta el directorio de tu proyecto. Luego, ejecuta:

   ```sh
   python -m venv venv
   ```

   Esto creará un directorio llamado `venv` en tu proyecto.

2. **Activar el entorno virtual:**

   ```sh
   .\venv\Scripts\activate
   ```

   Verás que el nombre del entorno virtual aparece en el prompt de tu terminal, indicando que el entorno está activo.

3. **Instalar Flet en el entorno virtual:**

   Con el entorno virtual activado, instala Flet:

   ```sh
   pip install flet
   ```

### Linux

1. **Crear un entorno virtual:**

   Abre una terminal y navega hasta el directorio de tu proyecto. Luego, ejecuta:

   ```sh
   python3 -m venv venv
   ```

   Esto creará un directorio llamado `venv` en tu proyecto.

2. **Activar el entorno virtual:**

   ```sh
   source venv/bin/activate
   ```

   Verás que el nombre del entorno virtual aparece en el prompt de tu terminal, indicando que el entorno está activo.

3. **Instalar Flet en el entorno virtual:**

   Con el entorno virtual activado, instala Flet:

   ```sh
   pip install flet
   ```

## Primer Proyecto con Flet

Con el entorno virtual configurado y Flet instalado, estamos listos para crear nuestra primera aplicación. Abre tu editor de texto o IDE preferido y crea un archivo llamado `app.py` con el siguiente contenido:

```python
import flet as ft

def main(page: ft.Page):
    page.title = "Hola, Flet!"
    lbl = ft.Text("¡Hola, mundo!")
    page.add(lbl)

ft.app(target=main)
```

Para ejecutar tu aplicación, asegúrate de que el entorno virtual esté activado y ejecuta:

```sh
python app.py
```

Deberías ver una ventana emergente con el mensaje "¡Hola, mundo!".

## Recursos Adicionales

- [Documentación de Flet](https://flet.dev/docs/)
- [Python Virtual Environments Documentation](https://docs.python.org/3/library/venv.html)
- [Tutoriales de Python](https://docs.python.org/3/tutorial/index.html)

Esperamos que disfrutes del taller y aprendas mucho sobre el desarrollo de interfaces gráficas con Flet. ¡Feliz codificación! 🚀

