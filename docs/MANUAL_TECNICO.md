# Manual técnico y de despliegue
## Sistema de Objetos Perdidos – Universidad Católica Luis Amigó

**Versión:** MVP académico  
**Tecnología:** Python, Flask, HTML y CSS  
**Repositorio:** https://github.com/samulondo/objetos-perdidos-ucatolica

### 1. Descripción del sistema

El sistema de Objetos Perdidos es una aplicación web desarrollada para apoyar el registro, consulta y gestión de objetos extraviados dentro de la Universidad Católica Luis Amigó.

El proyecto utiliza Flask como framework de desarrollo web. Cuenta con una pantalla de inicio de sesión que controla el acceso a la interfaz principal.

### 2. Requisitos de instalación

- Windows 10 o superior.
- Python 3.
- Git.
- Visual Studio Code (recomendado).
- Conexión a Internet para instalar las dependencias.

### 3. Estructura del proyecto

- `app.py`: servidor Flask y administración de rutas.
- `requirements.txt`: dependencias.
- `templates/login.html`: pantalla de inicio de sesión.
- `templates/terminos.html`: términos y condiciones.
- `templates/recuperar.html`: recuperación informativa de contraseña.
- `static/pagina_original.html`: interfaz principal.
- `static/style.css`: estilos.
- `static/logo_luis_amigo.png`: recurso gráfico institucional.

### 4. Instalación

Clonar el repositorio:

```powershell
git clone https://github.com/samulondo/objetos-perdidos-ucatolica.git
cd objetos-perdidos-ucatolica
```

Crear el entorno virtual:

```powershell
python -m venv .venv
```

Activar el entorno:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\.venv\Scripts\Activate.ps1
```

Instalar las dependencias:

```powershell
pip install -r requirements.txt
```

Ejecutar:

```powershell
python app.py
```

Abrir en el navegador:

`http://127.0.0.1:5000`

### 5. Configuración

El sistema permite configurar las siguientes variables de entorno:

- `SECRET_KEY`: clave para firmar las sesiones.
- `ADMIN_USER`: usuario administrador.
- `ADMIN_PASSWORD`: contraseña de acceso.

Los valores predeterminados son exclusivamente para demostración académica.

### 6. Rutas principales

| Ruta | Función |
|---|---|
| `/` | Página principal protegida |
| `/login` | Inicio de sesión |
| `/logout` | Cierre de sesión |
| `/terminos` | Términos y condiciones |
| `/recuperar` | Recuperación informativa |

### 7. Seguridad y limitaciones

La autenticación utiliza sesiones de Flask y credenciales configurables. La interfaz principal se entrega como un archivo HTML estático.

Esta versión corresponde a un MVP académico. No incluye todavía autenticación institucional, recuperación real por correo ni persistencia de datos mediante una base de datos.

Para un despliegue de producción se recomienda implementar almacenamiento persistente, gestión de usuarios, protección CSRF, HTTPS y controles adicionales de seguridad.