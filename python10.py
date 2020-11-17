a,b = list(map(int, input().split()))

if a % 2 == 0 and b % 2 == 1:
  print('YES')
elif a % 2 == 1 and b % 2 == 0:
  print('YES')
else:
  print('NO')
