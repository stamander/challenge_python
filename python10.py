
import re
s = input()
t = input()
res = re.search(s,t)
match_len = res.group()

print(len(match_len))




