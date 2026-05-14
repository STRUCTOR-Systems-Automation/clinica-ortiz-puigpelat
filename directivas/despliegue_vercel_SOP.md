# SOP: Despliegue de Sitio Estático en Vercel - Clínica Ortiz Puigpelat

## Objetivo
Desplegar de manera exitosa y profesional el sitio web estático de la Clínica Ortiz Puigpelat en la plataforma Vercel, asegurando que todos los recursos se carguen correctamente y el sitio sea accesible a través de GitHub.

## Entradas
- Archivo principal: `web-clinica-ortiz-puigpelat.html` (debe renombrarse a `index.html`).
- Carpeta de recursos: `assets/`.
- Scripts de utilidad: `update_html.py`.

## Lógica y Pasos
1. **Preparación del Entorno**:
    - Renombrar `web-clinica-ortiz-puigpelat.html` a `index.html`.
    - Verificar que todas las rutas de assets en el HTML sean relativas y correctas.
2. **Control de Versiones (Git)**:
    - Inicializar Git localmente (`git init`).
    - Crear un archivo `.gitignore` para excluir `.DS_Store`, `.tmp/`, etc.
    - Realizar el commit inicial.
3. **Sincronización con GitHub**:
    - Si `gh` CLI no está disponible, solicitar al usuario que cree un repositorio vacío en GitHub o intentar usar el navegador si es posible.
    - Vincular el repositorio local con el remoto.
    - Hacer push a la rama principal (`main`).
4. **Despliegue en Vercel**:
    - Conectar el repositorio de GitHub a un nuevo proyecto en Vercel.
    - Configurar el despliegue automático.

## Restricciones / Casos Borde
- **Entry Point**: Vercel busca `index.html` por defecto. Si no se renombra, hay que configurar el proyecto en Vercel manualmente.
- **Case Sensitivity**: Los nombres de archivos en `assets/` deben coincidir exactamente con las llamadas en el HTML (sensible a mayúsculas).
- **Git Config**: Verificar configuración de usuario local de Git.

## Trampas Conocidas
- Olvidar el `.gitignore`, subiendo basura del sistema operativo.
- No renombrar el archivo principal, causando un error 404 al visitar la URL raíz.
