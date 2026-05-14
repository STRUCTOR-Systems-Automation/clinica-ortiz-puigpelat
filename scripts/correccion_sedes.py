import os
import re

def update_clinics():
    html_file = 'web-clinica-ortiz-puigpelat.html'
    
    if not os.path.exists(html_file):
        print(f"Error: {html_file} no encontrado.")
        return

    with open(html_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Update stats counter from 3 to 2
    # <span class="counter" data-target="3">0</span>
    content = content.replace('data-target="3"', 'data-target="2"')

    # 2. Remove Marina Dent location card
    # We identify the exactly block by its content to avoid regex greediness issues
    
    # Let's find the start of the card
    search_str = '<h3>Clínica Marina Dent</h3>'
    if search_str in content:
        # Find the start of the <div class="location-card"> that contains this
        # We search backwards from the search_str
        pos = content.find(search_str)
        start_pos = content.rfind('<div class="location-card">', 0, pos)
        
        # Find the end of this div block. 
        # Since we know the structure, we can look for the closing </div> of location-card
        # It's followed by </div> (locations-grid) or another location-card.
        # Looking at the file, the Marina Dent card is the last one.
        
        # Exact block retrieval to be sure
        end_pattern = '      </div>\n    </div>\n  </div>\n</section>'
        # Actually, let's just find the next </div> after the location-body </div>
        
        # Better: identify the whole block as seen in view_file
        block_to_remove = """      <div class="location-card">
        <div class="location-map">
          <svg viewBox="0 0 200 120" fill="none" stroke="rgba(47, 143, 144, 0.35)" stroke-width="0.8">
            <path d="M0 45 L200 15 M0 85 L200 60 M0 110 L200 98"/>
            <path d="M60 0 L50 120 M140 0 L155 120"/>
            <rect x="70" y="40" width="40" height="30" fill="rgba(71,181,182,0.15)"/>
            <rect x="110" y="25" width="20" height="25" fill="rgba(71,181,182,0.1)"/>
          </svg>
          <div class="location-map-pin"></div>
          <div class="location-badge">Sede Marina Dent</div>
        </div>
        <div class="location-body">
          <h3>Clínica Marina Dent</h3>
          <div class="area">Zona Franca · Barcelona</div>
          <div class="location-info">
            <div class="location-info-row">
              <span class="location-info-icon">
                <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"/><circle cx="12" cy="10" r="3"/></svg>
              </span>
              <div><strong>Carrer Mineria 5-7, local</strong>08038 Barcelona</div>
            </div>
            <div class="location-info-row">
              <span class="location-info-icon">
                <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"/></svg>
              </span>
              <div><a href="tel:+34932968385"><strong>93 296 83 85</strong></a><a href="tel:+34606459827">Móvil 606 459 827</a></div>
            </div>
            <div class="location-info-row">
              <span class="location-info-icon">
                <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/></svg>
              </span>
              <div><strong>L-V · 9:30 – 13:30</strong>16:00 – 20:00</div>
            </div>
          </div>
          <a href="#cita" class="location-cta">Pedir cita aquí
            <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 12h14M13 5l7 7-7 7"/></svg>
          </a>
        </div>
      </div>"""
        
        if block_to_remove in content:
            content = content.replace(block_to_remove, "")
            print("Éxito: Se ha eliminado el bloque de Marina Dent.")
        else:
            # Fallback to a simpler search if indentation varies
            print("Aviso: El bloque exacto no coincidió, intentando con patrón más flexible.")
            content = re.sub(r'\s*<div class="location-card">.*?Marina Dent.*?</div>\s*</div>', '', content, flags=re.DOTALL)
    
    # Save results
    with open(html_file, 'w', encoding='utf-8') as f:
        f.write(content)
    print("Éxito: Archivo guardado.")

if __name__ == "__main__":
    update_clinics()
