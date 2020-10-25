import random

def poker(number):
  first = number[0:1]
  second = number[1:2]
  third = number[2:3]
  firth = number[3:4]
  
  if first == second == third == firth:
    print('Four Card')
  elif first == second == third:  #three card
    print('Three Card')
  elif second == third == firth:
    print('Three Card')
  elif first == second == firth:
    print('Three Card')
  elif first == second and third == firth: #Two Pair
    print('Two Pair')
  elif first == third and second == firth: #Two Pair
    print('Two Pair')
  elif first == firth and second == third: #Two Pair
    print('Two Pair')

  elif first == second:#Owe Pair
    print('One Pair')
  elif first == third:
    print('One Pair')
  elif first == firth:
    print('One Pair')
  elif second == third:
    print('One Pair')
  elif second == firth:
    print('One Pair')
  elif third == firth:
    print('One Pair')
  else:
    print('No Pair')


number = random.randrange(1000,10000)

print(number)

plays = input('手札を変更しますか？ yes or no:')


if plays == 'yes':
  number = random.randrange(1000,10000)
  number = str(number)

  poker(number)

elif plays == 'no':
  number = str(number)

  poker(number)


print(number)









 