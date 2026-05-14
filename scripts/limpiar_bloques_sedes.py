import os
import re

def clean_location_blocks():
    html_file = 'web-clinica-ortiz-puigpelat.html'
    with open(html_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Define SVGs
    email_svg = '<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"/><polyline points="22,6 12,13 2,6"/></svg>'
    whatsapp_svg = '<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 11.5a8.38 8.38 0 0 1-.9 3.8 8.5 8.5 0 1 1-7.6-11.4 8.28 8.28 0 0 1 3.5.8L21 3.5Z"/></svg>'
    clock_svg = '<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/></svg>'
    pin_svg = '<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"/><circle cx="12" cy="10" r="3"/></svg>'
    phone_svg = '<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"/></svg>'

    # Sede 1: Carles III
    c3_new_info = f"""            <div class="location-info-row">
              <span class="location-info-icon">{pin_svg}</span>
              <div><strong>Gran Vía Carles III 47, local</strong>08028 Barcelona</div>
            </div>
            <div class="location-info-row">
              <span class="location-info-icon">{phone_svg}</span>
              <div>
                <a href="tel:+34934393497"><strong>93 439 34 97</strong></a>
                <a href="https://wa.me/34693275830" style="display:flex;align-items:center;gap:4px;margin-top:2px;">{whatsapp_svg} 693 275 830</a>
              </div>
            </div>
            <div class="location-info-row">
              <span class="location-info-icon">{email_svg}</span>
              <div><a href="mailto:info1@clinicaortizpuigpelat.com">info1@clinicaortizpuigpelat.com</a></div>
            </div>
            <div class="location-info-row">
              <span class="location-info-icon">{clock_svg}</span>
              <div><strong>L-V · 9:30 – 13:30</strong>16:00 – 20:00</div>
            </div>"""

    # Sede 2: Tarradellas
    tarr_new_info = f"""            <div class="location-info-row">
              <span class="location-info-icon">{pin_svg}</span>
              <div><strong>Av. Josep Tarradellas 106 local</strong>08029 Barcelona</div>
            </div>
            <div class="location-info-row">
              <span class="location-info-icon">{phone_svg}</span>
              <div>
                <a href="tel:+34935154492"><strong>93 515 44 92</strong></a>
                <a href="https://wa.me/34669390046" style="display:flex;align-items:center;gap:4px;margin-top:2px;">{whatsapp_svg} 669 390 046</a>
              </div>
            </div>
            <div class="location-info-row">
              <span class="location-info-icon">{email_svg}</span>
              <div><a href="mailto:info2@clinicaortizpuigpelat.com">info2@clinicaortizpuigpelat.com</a></div>
            </div>
            <div class="location-info-row">
              <span class="location-info-icon">{clock_svg}</span>
              <div><strong>L-V · 9:30 – 13:30</strong>16:00 – 20:00</div>
            </div>"""

    # Replace the whole info block in Tarradellas
    # Find the start of Tarradellas body
    tarr_marker = '<h3>Clínica Tarradellas</h3>'
    tarr_start = content.find('<div class="location-info">', content.find(tarr_marker))
    tarr_end = content.find('</div>', content.find('location-cta', tarr_start)) # Search for end of info before the CTA
    # Actually, let's just find the closing tag of location-info
    # Since I know the structure, I'll find the next </a> of the CTA and search back for the </div> of location-info
    cta_pos = content.find('location-cta', tarr_start)
    info_end_pos = content.rfind('</div>', tarr_start, cta_pos)
    
    # Precise replacement for Tarradellas
    old_tarr_block = content[tarr_start : info_end_pos+6]
    content = content.replace(old_tarr_block, f'<div class="location-info">\n{tarr_new_info}\n          </div>')

    # Now for Carles III
    c3_marker = '<h3>Clínica Carles III</h3>'
    c3_start = content.find('<div class="location-info">', content.find(c3_marker))
    cta_pos_c3 = content.find('location-cta', c3_start)
    info_end_pos_c3 = content.rfind('</div>', c3_start, cta_pos_c3)
    
    old_c3_block = content[c3_start : info_end_pos_c3+6]
    content = content.replace(old_c3_block, f'<div class="location-info">\n{c3_new_info}\n          </div>')

    with open(html_file, 'w', encoding='utf-8') as f:
        f.write(content)
    print("Éxito: Bloques de información de sedes reconstruidos limpiamente.")

if __name__ == "__main__":
    clean_location_blocks()
