
i = list(map(int, input().split()))

start = i[0]

ride_time = i[1]

point = 0

money = [int(input()) for i in range(ride_time)]

for fare in money:
  


  if point > fare:
    point-=fare
  else:
    start-=fare

    point += int(fare/10) 
  print(start,point)




# for balance in money:

#   point = 0

#   start -= balance
#   point += int(balance/10)







#   if point <= 100:
#     balance-=100
    

  

#   print(start,point)



  



  