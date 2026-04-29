import glob
import re

html_files = glob.glob('*.html')

pattern = re.compile(r'<div class="mt-4 md:mt-0 space-x-4">.*?</div>', re.DOTALL)

for file in html_files:
    with open(file, 'r') as f:
        content = f.read()
    
    content = pattern.sub('', content)

    with open(file, 'w') as f:
        f.write(content)

print("Removed Privacy Policy and Terms of Service from footers.")
