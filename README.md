
# Sistema Punto de Venta con Django

Este proyecto es un sistema de punto de venta (POS) desarrollado con Django. Permite la gestión de productos, ventas, clientes y reportes, ideal para pequeñas y medianas empresas que necesitan controlar su inventario y registrar sus transacciones de forma sencilla y efectiva.

---

## Capturas 
### Inicio de sesión
![Login](img/login.png)
![Editar perfil](img/editar-perfil.png)

### Cajero
![Ventas](img/ventas.png)
![PDF](img/pdf.png)
![Nueva venta](img/nueva-venta.png)
![Productos](img/productos.png)


### Gerente
![Panel Gerente](img/panel-gerente.png)
![Graficos](img/graficos.png)
![Clientes](img/clientes.png)
![Nuevo cliente](img/forms-cliente.png)


### Administrador
![Panel Admin](img/panel-admin.png)
![Usuarios](img/usuarios.png)
---

## Objetivos del proyecto

- Gestionar productos y su inventario.
- Registrar ventas con desglose por productos.
- Control de usuarios y autenticación segura.
- Panel administrativo con visualización de datos.
- API REST para interacción externa (extensible).
- Reportes exportables (CSV, PDF o visuales).

---

## Tecnologías utilizadas

- Python 3.10+
- Django 4.x
- PostgreSQL o SQLite
- Bootstrap 5
- WeasyPrint (para PDF)

---

## Funcionalidades principales

- CRUD de productos y categorías
- Registro de clientes
- Registro de ventas y cálculo automático de totales
- Reducción de inventario tras venta
- Panel de historial de ventas por día/mes
- Exportación de tickets y reportes

---

## Instalación y ejecución

### 1. Clonar el repositorio

```bash
git clone https://github.com/tuusuario/django-pos-system.git
cd django-pos-system
```

### 2. Crear entorno virtual e instalar dependencias

```bash
python -m venv env
source env/bin/activate
pip install -r requirements.txt
```

### 3. Migraciones y superusuario

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```

### 4. Ejecutar el servidor

```bash
python manage.py runserver
```

---

## Estructura del proyecto

```
django-pos-system/
├── ventas/              # App de ventas
├── productos/           # App de productos
├── clientes/            # App de clientes
├── usuarios/            # App de autenticación
├── templates/           # HTML con Bootstrap
├── static/              # CSS, JS, imágenes
├── db.sqlite3           # Base de datos local
├── manage.py
└── requirements.txt
```

---

## Autoría

Proyecto desarrollado por Ana Chenoweth

---

## Licencia

Este proyecto está licenciado bajo la licencia MIT. Consulta el archivo [LICENSE](./LICENSE) para más detalles.
