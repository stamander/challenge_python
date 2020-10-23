
input_line = (input())
a = input_line[:1]
kigou = input_line[2:3]
b = input_line[4:5]
c = input_line[8:9]






if a == 'x':
  b = int(b)
  c = int(c)

  if kigou == '+':
    answer = c -b
  elif kigou == '-':
    answer = c+b

elif b == 'x':
  a = int(a)
  c = int(c)
  if kigou == '+':
    answer = c+a
  elif kigou == '-':
    answer  = (c - a) /-1

    answer=int(answer)


elif c == 'x':
  a = int(a)
  b = int(b)

  if kigou == '+':
    answer = a + b
  elif kigou == '-':
    answer = a-b

print(answer)



