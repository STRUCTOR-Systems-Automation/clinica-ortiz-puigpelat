import re

with open('web-clinica-ortiz-puigpelat.html', 'r') as f:
    content = f.read()

# Replace <div class="treatment-panel-info"> with <div class="treatment-info-card">
content = content.replace('<div class="treatment-panel-info">', '<div class="treatment-info-card">')
# Remove <div class="treatment-panel-imgs">
content = content.replace('          <div class="treatment-panel-imgs">\n', '')

# Remove closing tag of treatment-panel-imgs
# Given the structure:
#           </div>
#         </div>
#       </div>
#
#       <div class="treatment-row"

old_block = """          </div>
        </div>
      </div>

      <div class="treatment-row\""""

new_block = """        </div>
      </div>

      <div class="treatment-row\""""

content = content.replace(old_block, new_block)

# Handle the very last one (Endodoncia)
old_last = """          </div>
        </div>
      </div>
    </div>
  </div>
</section>"""

new_last = """        </div>
      </div>
    </div>
  </div>
</section>"""
content = content.replace(old_last, new_last)

with open('web-clinica-ortiz-puigpelat.html', 'w') as f:
    f.write(content)

