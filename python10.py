

N = int(input()) #1行目のNを取得する
s = [int(input()) for i in range(N)] #複数行の数値の入力を取得

for num in s:

  

  answer = [i for i in range(1, num+1) if num % i ==0]



  total_answer = sum(answer)-num



  if num == total_answer:
    print('perfect')

  elif num - total_answer == 1:
    print('nearly')

  else:
    print('neither')