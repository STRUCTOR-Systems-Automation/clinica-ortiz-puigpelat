import os

def refine_clinics():
    html_file = 'web-clinica-ortiz-puigpelat.html'
    
    if not os.path.exists(html_file):
        print(f"Error: {html_file} no encontrado.")
        return

    with open(html_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Define SVG and HTML snippets
    email_svg = '<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"/><polyline points="22,6 12,13 2,6"/></svg>'
    whatsapp_svg = '<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 11.5a8.38 8.38 0 0 1-.9 3.8 8.5 8.5 0 1 1-7.6-11.4 8.28 8.28 0 0 1 3.5.8L21 3.5Z"/></svg>'
    
    # 1. Update Carles III (Sede 1)
    # Schedule
    content = content.replace('<div><strong>L-V · 9:30 – 20:00</strong>Abrimos al mediodía</div>', 
                             '<div><strong>L-V · 9:30 – 13:30</strong>16:00 – 20:00</div>')
    
    # Add Email 1 and improve Mobile/WhatsApp
    c3_phone_block_old = '<div><a href="tel:+34934393497"><strong>93 439 34 97</strong></a><a href="tel:+34693275830">Móvil 693 275 830</a></div>'
    c3_phone_block_new = (
        '<div>'
        '<a href="tel:+34934393497"><strong>93 439 34 97</strong></a>'
        '<a href="https://wa.me/34693275830" style="display:flex;align-items:center;gap:4px;margin-top:2px;">'
        f'{whatsapp_svg} 693 275 830'
        '</a>'
        '</div>'
    )
    content = content.replace(c3_phone_block_old, c3_phone_block_new)
    
    # Email block for C3
    email1_html = (
        '            <div class="location-info-row">\n'
        f'              <span class="location-info-icon">{email_svg}</span>\n'
        '              <div><a href="mailto:info1@clinicaortizpuigpelat.com">info1@clinicaortizpuigpelat.com</a></div>\n'
        '            </div>'
    )
    # Insert before schedule block
    content = content.replace('<div><strong>L-V · 9:30 – 13:30</strong>16:00 – 20:00</div>', 
                             '<div><strong>L-V · 9:30 – 13:30</strong>16:00 – 20:00</div>\n' + email1_html)

    # 2. Update Tarradellas (Sede 2)
    # Address
    content = content.replace('<strong>Av. Josep Tarradellas 106-108</strong>', '<strong>Av. Josep Tarradellas 106 local</strong>')
    
    # Add Email 2 and improve Mobile/WhatsApp
    tarr_phone_block_old = '<div><a href="tel:+34935154492"><strong>93 515 44 92</strong></a><a href="tel:+34669390046">Móvil 669 390 046</a></div>'
    tarr_phone_block_new = (
        '<div>'
        '<a href="tel:+34935154492"><strong>93 515 44 92</strong></a>'
        '<a href="https://wa.me/34669390046" style="display:flex;align-items:center;gap:4px;margin-top:2px;">'
        f'{whatsapp_svg} 669 390 046'
        '</a>'
        '</div>'
    )
    content = content.replace(tarr_phone_block_old, tarr_phone_block_new)
    
    # Email block for Tarradellas
    email2_html = (
        '            <div class="location-info-row">\n'
        f'              <span class="location-info-icon">{email_svg}</span>\n'
        '              <div><a href="mailto:info2@clinicaortizpuigpelat.com">info2@clinicaortizpuigpelat.com</a></div>\n'
        '            </div>'
    )
    # Insert at similar position as C3 email
    # Find the Tarradellas schedule block
    tarr_schedule = '<div><strong>L-V · 9:30 – 13:30</strong>16:00 – 20:00</div>'
    content = content.replace(tarr_schedule, tarr_schedule + '\n' + email2_html, 1) # Only first occurrence (Tarradellas comes first in file)

    with open(html_file, 'w', encoding='utf-8') as f:
        f.write(content)
    print("Éxito: Datos de ambas sedes sincronizados perfectamente con la imagen oficial.")

if __name__ == "__main__":
    refine_clinics()
