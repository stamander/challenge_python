
import re #reモジュールのインポート

n = int(input()) #1行目のNを取得する
word = input()
s = [input() for i in range(n)] 

i = 0


for language in s:

  if re.search(word, language):
    print(language)
    i+=1
if i == 0:
  print('None')




