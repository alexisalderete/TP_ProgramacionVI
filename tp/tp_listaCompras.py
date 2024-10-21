import flet as ft

def main(page):
    # Definir ancho y alto de la ventana (usando las nuevas propiedades)
    page.window.width = 600  # ancho de la ventana
    page.window.height = 400  # alto de la ventana
    page.title = "Lista de Compras"  # título
    page.theme_mode = ft.ThemeMode.LIGHT  # tema blanco

    # Inicializamos la lista de tareas en el objeto page
    page.tasks = []

    # Mensaje de error
    msj_error = ft.Text(value="", color="red")

    # Función para actualizar la lista en la interfaz
    def update_tasks():
        task_list.controls.clear()  # Limpiar lista actual
        for task in page.tasks:  # Usar page.tasks
            task_list.controls.append(task)  # Añadir los checkboxes
        task_list.update()

    # Botón para agregar tarea
    def add_clicked(e):
        msj_error.value = ""
        if task_input.value.strip() == "":
            msj_error.value = "Por favor, ingrese un producto"
        else:
            task_checkbox = ft.Checkbox(label=task_input.value, value=False)
            page.tasks.append(task_checkbox)  # Agregar a la lista de tareas en page
            task_input.value = ""
            task_input.focus()
            update_tasks()  # Actualizar la lista de tareas
        
        msj_error.update()

    # Botón para modificar tarea seleccionada
    def edit_clicked(e):
        msj_error.value = ""
        if task_input.value.strip() == "":
            msj_error.value = "Por favor, seleccione una tarea y edítela"
        else:
            # Buscar la tarea seleccionada y modificarla
            for task in page.tasks:  # Usar page.tasks
                if task.value:  # Si el checkbox está seleccionado
                    task.label = task_input.value  # Cambiar la etiqueta
                    task.value = False  # Desmarcar
                    task_input.value = ""  # Limpiar el campo de texto
                    task_input.focus()
                    update_tasks()  # Actualizar lista de tareas
                    break
            else:
                msj_error.value = "Por favor, seleccione una tarea para modificar"
        msj_error.update()

    # Botón para eliminar tareas seleccionadas
    def delete_clicked(e):
        # Crear una nueva lista solo con tareas no seleccionadas (checkbox no marcado)
        page.tasks = [task for task in page.tasks if not task.value]  # Usar page.tasks
        update_tasks()  # Actualizar la lista de tareas
        task_input.focus()

    # Campo para agregar tarea
    task_input = ft.TextField(hint_text="¿Qué necesitas?", width=300)

    # Botones
    add_button = ft.ElevatedButton("Agregar", on_click=add_clicked)
    edit_button = ft.ElevatedButton(text="Modificar", on_click=edit_clicked)
    delete_button = ft.ElevatedButton(text="Eliminar", on_click=delete_clicked)

    # Lista dinámica de tareas
    task_list = ft.Column()

    # Crear una cabecera con el logo e imagen (texto o imagen)
    logo = ft.Image(src="/logo.png", width=100, height=100)
    header_text = ft.Text("Bienvenidos a la App", size=30, weight=ft.FontWeight.BOLD)

    # Organizar cabecera en una columna
    header = ft.Column(
        [logo, header_text],
        alignment=ft.MainAxisAlignment.CENTER, 
        horizontal_alignment=ft.CrossAxisAlignment.CENTER
    )

    # Cuerpo de la aplicación
    body = ft.Column(
        [
            task_input,
            ft.Row([add_button, edit_button, delete_button], alignment=ft.MainAxisAlignment.CENTER),
            msj_error,
            task_list  # Añadimos la lista de tareas
        ],
        alignment=ft.MainAxisAlignment.CENTER,  # Centrarmos los contenidos
        horizontal_alignment=ft.CrossAxisAlignment.CENTER # Centrarmos los contenidos
    )

    # Añadir los elementos a la aplicación
    page.add(
        ft.Column(
            [
                header,  # Para que muestre el texto primero
                ft.Divider(height=20),  # Agrega un divisor para separar el logo de la sección
                body  # Cuerpo que contiene el resto de los elementos
            ],
            alignment=ft.MainAxisAlignment.CENTER,  # Centra todo verticalmente en la página
            horizontal_alignment=ft.CrossAxisAlignment.CENTER  # Centra todo horizontalmente
        )
    )

ft.app(
    main,
    assets_dir="img"  # Para que funcione la fuente de la imagen
)