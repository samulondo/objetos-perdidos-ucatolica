# Sistema de Objetos Perdidos – Universidad Católica Luis Amigó

## Descripción

Este proyecto es un MVP de un sistema de objetos perdidos para la Universidad Católica Luis Amigó. Su propósito es facilitar la consulta y gestión de información relacionada con objetos extraviados y encontrados dentro de la institución.

El proyecto integra una interfaz web con un sistema de autenticación desarrollado en Python utilizando Flask.

## Tecnologías utilizadas

- Python.
- Flask.
- HTML5.
- CSS3.
- Git y GitHub.

## Estructura del proyecto

```text
objetos_perdidos/
├── docs/
│   ├── MANUAL_TECNICO.md
│   ├── MANUAL_USUARIO.md
│   ├── INFORME_PRUEBAS.md
│   └── PLAN_MANTENIMIENTO.md
├── static/
│   ├── logo_luis_amigo.png
│   ├── pagina_original.html
│   └── style.css
├── templates/
│   ├── login.html
│   ├── recuperar.html
│   └── terminos.html
├── app.py
├── requirements.txt
└── .gitignore
```

## Requisitos

- Python 3 instalado.
- pip.
- Navegador web.
- Git (opcional, para clonar el repositorio).

## Instalación y ejecución

### 1. Clonar el repositorio

```bash
git clone https://github.com/samulondo/objetos-perdidos-ucatolica.git
cd objetos-perdidos-ucatolica
```

### 2. Crear el entorno virtual

En Windows:

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

### 3. Instalar dependencias

```powershell
pip install -r requirements.txt
```

### 4. Ejecutar la aplicación

```powershell
python app.py
```

### 5. Abrir en el navegador

Ingresar a:

http://127.0.0.1:5000

## Credenciales de demostración

- **Usuario:** admin
- **Contraseña:** admin123

Las credenciales pueden configurarse mediante las variables de entorno `ADMIN_USER` y `ADMIN_PASSWORD`.

También se recomienda configurar `SECRET_KEY` con un valor seguro.

## Funcionalidades implementadas

- Inicio de sesión.
- Validación de credenciales.
- Control de acceso a la página principal.
- Cierre de sesión.
- Redirección al login cuando no existe una sesión autenticada.
- Interfaces de términos y condiciones y recuperación de contraseña.

## Documentación

Los documentos del proyecto se encuentran en la carpeta `docs`:

- Manual técnico.
- Manual de usuario.
- Informe de pruebas.
- Plan de mantenimiento.

## Alcance del MVP

Esta versión es un prototipo funcional para demostrar la interfaz y el flujo de autenticación. No debe considerarse todavía un sistema de producción. La persistencia de información, la recuperación real de contraseñas y otras integraciones requieren desarrollo adicional.

## Repositorio

https://github.com/samulondo/objetos-perdidos-ucatolica