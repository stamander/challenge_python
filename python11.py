N = int(input())

s = [int(input()) for i in range(N)]

ans = 0
i =1

for st in s:
  ans +=abs(st-i)

  i=st

print(ans)

# print(sum(s)-1)



# n = gets.to_i

# ans = 0
# i = 1
# n.times{
#     a = gets.to_i
#     ans += (a-i).abs
#     i = a
# }

# puts ans