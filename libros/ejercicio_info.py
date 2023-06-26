"""
Aquí tienes una consigna para un ejercicio de Django que involucra la creación de un CRUD (Crear, Leer, Actualizar, Eliminar) y el uso de formularios HTML para un modelo que tiene un campo ManyToMany:

Modelo:

    Crea un modelo llamado "Libro" que tenga los siguientes campos:
        Título (CharField)
        Autor (ManyToManyField al modelo "Autor")
        Descripción (TextField)
        Fecha de publicación (DateField)
        Cantidad de páginas (IntegerField)

Vistas:

    Crea las vistas correspondientes para realizar las operaciones CRUD (Crear, Leer, Actualizar, Eliminar) de los libros.
    La vista principal debe mostrar una lista de todos los libros existentes, con la opción de agregar, editar y eliminar libros.
    La vista de creación debe mostrar un formulario para agregar un nuevo libro.
    La vista de actualización debe mostrar un formulario prellenado con los datos del libro a editar.
    La vista de eliminación debe confirmar la eliminación del libro seleccionado.

Formularios HTML:

    Crea un formulario HTML para la creación y actualización de libros.
    El formulario debe incluir campos para el título, descripción, fecha de publicación y cantidad de páginas.
    Para el campo de autor, utiliza un campo de selección múltiple para permitir la selección de uno o varios autores existentes.

Tareas:

    Define el modelo "Libro" en tu archivo models.py y realiza las migraciones necesarias.
    Crea las vistas correspondientes en tu archivo views.py para las operaciones CRUD.
    Implementa los formularios HTML en tu archivo forms.py para la creación y actualización de libros.
    Crea las plantillas HTML correspondientes en tu directorio de plantillas para mostrar y procesar los formularios y las vistas.
    Configura las URL en tu archivo urls.py para asociar las vistas a las rutas adecuadas.

Recuerda importar los modelos, formularios y vistas correspondientes en los archivos donde los necesites. Además, asegúrate de configurar correctamente las rutas URL para cada vista.

Este ejercicio te permitirá practicar la creación de un CRUD completo utilizando Django, trabajar con campos ManyToMany y utilizar formularios HTML para interactuar con los datos. Puedes expandir el ejercicio agregando funcionalidades adicionales, como la búsqueda de libros o la paginación de la lista de libros.

"""