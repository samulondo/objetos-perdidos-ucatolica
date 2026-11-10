# Plan de mantenimiento – Sistema de objetos perdidos

## 1. Objetivo

Establecer actividades básicas para conservar el funcionamiento del sistema de objetos perdidos, facilitar futuras actualizaciones y prevenir errores durante su ejecución.

## 2. Tipos de mantenimiento

### 2.1. Mantenimiento correctivo

Consiste en identificar y solucionar errores que afecten el funcionamiento del sistema.

Ejemplos:
- Corregir errores al iniciar sesión.
- Solucionar problemas de visualización de imágenes o estilos.
- Corregir errores en las rutas de Flask.
- Resolver problemas al cargar la página principal.

### 2.2. Mantenimiento preventivo

Busca reducir la posibilidad de que aparezcan errores.

Actividades:
- Revisar periódicamente el código.
- Verificar que las dependencias estén actualizadas y sean compatibles.
- Comprobar que los archivos del proyecto estén organizados.
- Mantener copias de seguridad del código.
- Revisar que los archivos sensibles no se publiquen en GitHub.

### 2.3. Mantenimiento evolutivo

Consiste en incorporar nuevas funcionalidades de acuerdo con las necesidades de los usuarios.

Posibles mejoras:
- Conectar el sistema a una base de datos.
- Implementar recuperación real de contraseñas.
- Incorporar roles y permisos de usuario.
- Mejorar los filtros y las búsquedas.
- Implementar notificaciones reales.
- Permitir registrar y consultar objetos con información persistente.

## 3. Procedimiento para actualizar el proyecto

1. Obtener la última versión del repositorio.
2. Crear una copia de seguridad antes de realizar cambios importantes.
3. Realizar las modificaciones necesarias.
4. Ejecutar la aplicación localmente.
5. Probar las funcionalidades afectadas.
6. Registrar los cambios en Git.
7. Subir los cambios al repositorio remoto.

Comandos básicos:

```powershell
git pull origin main
git status
git add .
git commit -m "Descripción de la actualización"
git push origin main
```

## 4. Problemas frecuentes

| Problema | Posible solución |
|---|---|
| No inicia la aplicación | Verificar que el entorno virtual esté activado y las dependencias instaladas. |
| No encuentra Flask | Ejecutar `pip install -r requirements.txt`. |
| No permite iniciar sesión | Verificar las credenciales y las variables de entorno. |
| No carga el diseño | Revisar la ubicación de `static/style.css`. |
| No carga el HTML principal | Comprobar que exista `static/pagina_original.html`. |
| No permite subir cambios a GitHub | Revisar la conexión remota y el estado del repositorio. |

## 5. Seguridad y recomendaciones

- No publicar el archivo `.env`.
- No compartir contraseñas de administración.
- Cambiar las credenciales de demostración antes de cualquier uso real.
- Utilizar una clave secreta segura para las sesiones.
- Realizar pruebas después de cada modificación.
- Mantener actualizado el repositorio.

## 6. Alcance del mantenimiento

Este plan corresponde a la versión MVP del proyecto. Las actividades propuestas permiten mantener el prototipo y sirven como base para futuras versiones con almacenamiento persistente, autenticación robusta y funcionalidades adicionales.