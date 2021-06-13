# string = input()

# print(string[0] + ' ' + string[1])



# 入力例1
# 2
# read



# スライス使った一つ飛ばし

# nに数を代入
n = int(input()) - 1
# stringに代入
string = input() 

if n + 1 < len(string):
    print(string[n] + ' ' + string[n + 1])

# 出力例1
# e a