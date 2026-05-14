import os

def update_cta_text():
    html_file = 'web-clinica-ortiz-puigpelat.html'
    old_text = 'Pedir cita sin compromiso'
    new_text = 'Agenda tu cita'
    
    if not os.path.exists(html_file):
        print(f"Error: {html_file} no encontrado.")
        return

    with open(html_file, 'r', encoding='utf-8') as f:
        content = f.read()

    if old_text in content:
        new_content = content.replace(old_text, new_text)
        with open(html_file, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Éxito: Se ha cambiado '{old_text}' por '{new_text}'.")
    else:
        print(f"Aviso: No se encontró el texto '{old_text}' en el archivo.")

if __name__ == "__main__":
    update_cta_text()
