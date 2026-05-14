# SOP: Cambio de Texto en CTA

## Objetivo
Actualizar el texto de los botones de "Call to Action" (CTA) en el sitio web de la clínica para mejorar la conversión.

## Entradas
- Archivo: `web-clinica-ortiz-puigpelat.html`
- Texto antiguo: "Pedir cita sin compromiso"
- Texto nuevo: "Agenda tu cita"

## Lógica de Ejecución
1. El script de Python abrirá el archivo HTML.
2. Usará un reemplazo de cadena simple para cambiar "Pedir cita sin compromiso" por "Agenda tu cita".
3. Guardará el archivo.
4. Se verificará que el texto haya sido actualizado.

## Restricciones y Casos Borde
- Asegurar que no se modifiquen partes del código HTML accidentalmente (aunque un reemplazo de texto simple suele ser seguro para este tipo de cadenas).
- Mantener los iconos adyacentes al texto intactos.

## Verificación
- Cargar el archivo y comprobar la ausencia del texto original.
