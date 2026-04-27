import glob

html_files = glob.glob('*.html')

for file in html_files:
    with open(file, 'r') as f:
        content = f.read()

    # 1. max-w-7xl -> max-w-[1200px] in the footer
    content = content.replace(
        'class="max-w-7xl mx-auto grid grid-cols-1 md:grid-cols-4 gap-10"',
        'class="max-w-[1200px] mx-auto grid grid-cols-1 md:grid-cols-4 gap-10"'
    )
    content = content.replace(
        'class="max-w-7xl mx-auto mt-12 pt-8 border-t border-blue-800 text-sm text-center md:text-left flex flex-col md:flex-row justify-between items-center text-blue-300"',
        'class="max-w-[1200px] mx-auto mt-12 pt-8 border-t border-blue-800 text-sm text-center md:text-left flex flex-col md:flex-row justify-between items-center text-blue-300"'
    )

    # 2. remove the mb-6 from the description to match removal of icons
    content = content.replace(
        'class="text-sm opacity-80 leading-relaxed mb-6"\n            data-i18n="footer_desc"',
        'class="text-sm opacity-80 leading-relaxed"\n            data-i18n="footer_desc"'
    )

    # 3. remove the social media section completely
    social_block = """          <div class="flex space-x-4">
            <a
              href="#"
              class="w-10 h-10 rounded-full bg-blue-800 flex items-center justify-center hover:bg-white hover:text-primary transition duration-300"
            >
              <i class="fa-brands fa-linkedin-in"></i>
            </a>
            <a
              href="#"
              class="w-10 h-10 rounded-full bg-blue-800 flex items-center justify-center hover:bg-white hover:text-primary transition duration-300"
            >
              <i class="fa-brands fa-facebook-f"></i>
            </a>
            <a
              href="#"
              class="w-10 h-10 rounded-full bg-blue-800 flex items-center justify-center hover:bg-white hover:text-primary transition duration-300"
            >
              <i class="fa-brands fa-instagram"></i>
            </a>
          </div>"""
    content = content.replace(social_block, '')

    with open(file, 'w') as f:
        f.write(content)

print("Done")
