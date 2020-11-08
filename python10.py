time = int(input())
result = 0

for i in range(time):
  number = input()
  array = number.split()

  if array[0]==array[1]:
    result += int(array[0])*int(array[1])
  else:
    result +=int(array[0])+int(array[1])

print(result)

