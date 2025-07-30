# 📱 Python Flask Web v3

Este proyecto es una aplicación web que realiza operaciones **CRUD** y presenta **gráficos de usuarios** como nueva funcionalidad agregada en esta versión.

---

## ✨ Características Principales

- ✅ CRUD (Crear, Leer, Actualizar, Eliminar) completo de usuarios.
- ✅ Módulo de gráficos estadísticos interactivos.
- ✅ Interfaz web intuitiva y responsive.
- ✅ Base de datos SQLite liviana y fácil de usar.

---

## 🚀 Tecnologías Utilizadas

| Tecnología | Descripción                                   |
| ---------- | --------------------------------------------- |
| Python     | Backend de la aplicación                      |
| Flask      | Framework web ligero en Python                |
| Jinja2     | Motor de plantillas HTML                      |
| HTML/CSS   | Estructura y estilos del frontend             |
| JavaScript | Interacción dinámica y generación de gráficos |
| SQLite     | Base de datos embebida                        |

---

## 📅 Estructura del Proyecto

```
Python-Flask-Web_v3/
├── app.py
├── templates/
│   ├── index.html
│   ├── create_user.html
│   ├── update_user.html
│   └── charts.html
├── static/
│   ├── css/
│   └── js/
├── database.db
├── requirements.txt
└── README.md
```

---

## 🚡 Instalación Local (Desarrollo)

### 1. Clonar el Repositorio

```bash
git clone https://github.com/sebastian2161/Python-Flask-Web_v3.git
cd Python-Flask-Web_v3
```

### 2. Crear entorno virtual (opcional pero recomendado)

```bash
python3 -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
```

### 3. Instalar dependencias

```bash
Librerias Python
```

### 4. Ejecutar la aplicación

```bash
python run2.py
```

### 5. Abrir en navegador web

```
http://127.0.0.1:3000
```

---

## 📊 Visualización de Gráficos

- La página `charts.html` permite ver estadísticas de los usuarios.
- Se pueden utilizar librerías como **Chart.js** o **Google Charts** para mostrar datos visuales.

---

## 🚧 Despliegue (Producción)

- Puedes desplegarlo en servicios como **Cloud Run**, **Heroku**, **Render**, o **Compute Engine**.
- Crear un `Dockerfile` si deseas empaquetarlo como contenedor.
- Configurar variables de entorno y HTTPS en producción.

---

## 📊 Base de Datos SQLite

- Se crea automáticamente en la primera ejecución (`database.db`).
- Puedes utilizar herramientas como **DB Browser for SQLite** para editar o visualizar.

---

## 📢 Recursos Adicionales

- [Flask Oficial](https://flask.palletsprojects.com/)
- [Jinja2 Templates](https://jinja.palletsprojects.com/)
- [SQLite Docs](https://www.sqlite.org/docs.html)
- [Chart.js para Gráficos](https://www.chartjs.org/)

---

## 👨‍💼 Autor y Repositorio

- GitHub: [Python-Flask-Web\_v3](https://github.com/sebastian2161/Python-Flask-Web_v3)
- Desarrollador: [sebastian2161](https://github.com/sebastian2161)

---

## 🚧 Licencia

Este proyecto es de código abierto. Consulta el archivo LICENSE.


