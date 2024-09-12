# Proyecto Django API - CRUD de Tareas
Este proyecto es una API desarrollada con Django y Django Rest Framework (DRF) que permite realizar operaciones CRUD (Crear, Leer, Actualizar, Eliminar) en un recurso llamado "Tareas".

## Requisitos Previos
- Python 3.8+
- pip
- Virtualenv (opcional pero recomendado)
- Git (opcional para clonar este repositorio)

## Instrucciones de Configuración
1. Clonar el repositorio (opcional):
```bash
git clone https://github.com/jpc0099/Icarus.git
cd icarus
```
2. Crear un entorno virtual

Es recomendable crear un entorno virtual para manejar las dependencias de tu proyecto sin afectar otras instalaciones de Python en tu máquina.

 ```bash
# Crear el entorno virtual
python -m venv env

# Activar el entorno virtual
# En Windows
env\Scripts\activate

# En macOS/Linux
source env/bin/activate`
```

3. Instalar dependencias

Instala las dependencias necesarias usando el archivo requirements.txt

```bash
pip install -r requirements.txt
```
4. Crear el archivo .env

Crea un archivo llamado .env en el mismo nivel que tu archivo .gitignore y agrega las siguientes configuraciones básicas:

```plaintext
SECRET_KEY='tu_secret_key_generada_aquí'
DEBUG=True
```
5. Configurar la Base de Datos

Ejecuta las migraciones iniciales para configurar la base de datos SQLite:
```bash
python manage.py makemigrations
python manage.py migrate
```
Nota: Si al ejecutar el primer comando, te muestra que no hay cambios detectados, tendrás que ejecutar primero el comando: `python manage.py makemigrations Tareas --empty`
6. Crear un Superusuario (Opcional para administración)

Si quieres acceder al panel de administración de Django, crea un superusuario:
```bash
python manage.py createsuperuser
```
Sigue las instrucciones y proporciona un nombre de usuario, email y contraseña.

7. Ejecutar el Servidor

Inicia el servidor local de Django:
```bash
python manage.py runserver
```

El servidor correrá en http://127.0.0.1:8000/. Puedes acceder a los endpoints de la API desde ahí.


## Probar la API con Insomnia o Postman
Se recomienda usar Insomnia o Postman para interactuar con la API y probar los endpoints.

Ejemplos de Solicitudes:

### GET - Obtener todas las tareas
URL: http://127.0.0.1:8000/api/tareas/

Método: GET



### POST - Crear una nueva tarea
URL: http://127.0.0.1:8000/api/tareas/

Método: POST

Headers:

Content-Type: application/json

Body:

```json
{
  "titulo": "Leer un libro",
  "descripcion": "Leer 30 páginas de ciencia ficción",
  "completada": false
}
```

### PUT - Actualizar una tarea existente
URL: http://127.0.0.1:8000/api/tareas/1/

Método: PUT

Headers:

Content-Type: application/json

Body:

```json
{
  "titulo": "Leer un libro actualizado",
  "descripcion": "Leer 50 páginas de ciencia ficción",
  "completada": true
}
```

### DELETE - Eliminar una tarea
URL: http://127.0.0.1:8000/api/tareas/1/

Método: DELETE
