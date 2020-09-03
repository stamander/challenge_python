
# -*- coding: utf-8 -*-
 


try:
  a = input("type a number:")
  b = input("type b number:")

  a = int(a)
  b = int(b)
  print (a/b)
except (ZeroDivisionError,ValueError):
  print("bに0を入れたり、数値データを入れたりしたでしょ?だから計算できないよ")