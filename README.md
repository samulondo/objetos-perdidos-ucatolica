# Objetos Perdidos — Universidad Católica Luis Amigó

Esta versión integra el login institucional con el HTML original de Objetos Perdidos.

## Importante
- La pantalla principal se sirve desde `static/pagina_original.html` **sin modificar su contenido**.
- El login y las páginas de términos/recuperación están implementados con Flask.
- Las funciones y el diseño del HTML original se mantienen tal como estaban en el archivo entregado.
- El HTML original guarda sus datos en memoria del navegador; al recargar la página, los registros creados durante la sesión pueden reiniciarse. No se agregó una base de datos ni se reescribió su lógica para respetar el archivo original.

## Ejecutar en Windows PowerShell

```powershell
python -m venv .venv
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python app.py
```

Abrir: http://127.0.0.1:5000

## Credenciales de demostración
- Usuario: `admin`
- Contraseña: `admin123`

Se pueden cambiar definiendo las variables de entorno `ADMIN_USER`, `ADMIN_PASSWORD` y `SECRET_KEY`.

## Cerrar sesión
La ruta de cierre es `http://127.0.0.1:5000/logout`. No se añadió un botón al HTML original para no alterar su diseño.

> Esta autenticación es únicamente para demostración académica. No usar en producción sin implementar almacenamiento seguro de contraseñas, protección CSRF, HTTPS y controles adicionales.
