N = int(input()) #1行目のNを取得する
s = [int(input()) for i in range(N)] #複数行の数値の入力を取得

result =0

for array in s:
  if array >= 5:
    result +=array

print(result)
