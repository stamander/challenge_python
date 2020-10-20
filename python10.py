

i = list(map(int, input().split()))

N = int(i[0])
Decimal_number = int(i[1])

select_number = [int(input()) for i in range(N)]



Binary_number = bin(Decimal_number)[2:]

str_Binary_number = str(Binary_number)

for select_numbers in select_number :

  print(str_Binary_number[-select_numbers])

