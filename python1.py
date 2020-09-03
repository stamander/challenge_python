
# -*- coding: utf-8 -*-
 

a = input("type a number:")
b = input("type b number:")

a = int(a)
b = int(b)

try:
  print (a/b)
except ZeroDivisionError:
  print("b canot be zero")