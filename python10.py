nums = input().split()
string = input()

print(string[0:int(nums[0]) - 1], end='')
print(string[int(nums[0]) - 1:int(nums[1])].upper(), end='')
print(string[int(nums[1]):])