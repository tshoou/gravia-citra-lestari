import os
import glob
import re

# 1. Update about.html Company Group to use data-i18n
about_path = 'about.html'
with open(about_path, 'r') as f:
    about_html = f.read()

about_html = about_html.replace(
    '<p class="text-gray-500 font-medium text-[15px] leading-snug">The Holding Company of<br />Medical Equipment Distributor and<br />Aesthetics Clinic</p>',
    '<p class="text-gray-500 font-medium text-[15px] leading-snug" data-i18n="net_gravia_desc">The Holding Company of<br />Medical Equipment Distributor and<br />Aesthetics Clinic</p>'
)
about_html = about_html.replace(
    '<li>Holistic Treatment Clinic</li>',
    '<li data-i18n="net_gc_bullet1">Holistic Treatment Clinic</li>'
)
about_html = about_html.replace(
    '<li>Modern and Advance Clinic Equipment</li>',
    '<li data-i18n="net_gc_bullet2">Modern and Advance Clinic Equipment</li>'
)
about_html = about_html.replace(
    '<li>Trusted Distributor of IVD & Medical Devices</li>',
    '<li data-i18n="net_dis_bullet1">Trusted Distributor of IVD & Medical Devices</li>'
)
about_html = about_html.replace(
    '<li>Distributor of Panatha Citra Lestari (PDN / AKD)</li>',
    '<li data-i18n="net_dis_bullet2">Distributor of Panatha Citra Lestari (PDN / AKD)</li>'
)
about_html = about_html.replace(
    '<li>A Professional, Quality, Reliable and Trusted Medical Equipment Company in Indonesia</li>',
    '<li data-i18n="net_pan_bullet1">A Professional, Quality, Reliable and Trusted Medical Equipment Company in Indonesia</li>'
)

with open(about_path, 'w') as f:
    f.write(about_html)


# 2. Update products.html to add data-i18n to sterilization and hygiene categories
prod_path = 'products.html'
with open(prod_path, 'r') as f:
    prod_html = f.read()

prod_html = prod_html.replace(
    'data-category="sterilization">Sterilization & Infection Control</button>',
    'data-category="sterilization" data-i18n="cat_sterilization">Sterilization & Infection Control</button>'
)
prod_html = prod_html.replace(
    'data-category="hygiene">Hygiene Equipment</button>',
    'data-category="hygiene" data-i18n="cat_hygiene">Hygiene Equipment</button>'
)

with open(prod_path, 'w') as f:
    f.write(prod_html)


# 3. Update all footers across all HTML files
html_files = glob.glob('*.html')
footer_regex = re.compile(
    r'(<li>\s*<a href="products\.html" class="hover:text-white transition" data-i18n="cat_centrifuges">Clinical & Research Centrifuges</a>\s*</li>)',
    re.MULTILINE
)

new_footer_items = r'''\1
          <li>
            <a href="products.html" class="hover:text-white transition" data-i18n="cat_sterilization">Sterilization & Infection Control</a>
          </li>
          <li>
            <a href="products.html" class="hover:text-white transition" data-i18n="cat_hygiene">Hygiene Equipment</a>
          </li>'''

for file in html_files:
    with open(file, 'r') as f:
        content = f.read()
    
    # We use regex sub to replace the cat_centrifuges li with itself + the new ones
    content = footer_regex.sub(new_footer_items, content)
    
    with open(file, 'w') as f:
        f.write(content)

print("Updated HTML files.")
