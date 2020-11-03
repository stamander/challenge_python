import re

source = '''飯田集志'''

print(re.findall('[a-z,A-Z]+',source))