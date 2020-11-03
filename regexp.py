import re

source = '''飯田集志'''

print(re.findall('[^\u\l]+',source))