students,reports = list(map(int, input().split())) 

result = 0


for i in range(students):
  std_in = input()
  array = std_in.split()
  day = int(array[0])
  cleare = int(array[1])
  haiten=100/reports

  point = haiten * cleare
  


  if day >= 10:
    result = point*0
  elif day>=1 and day <=9:
    result =point*0.8
  else:
    result=point




    if result >= 80:
      asess = 'A'
    elif  result >=70 and result <= 79:
      asess = 'B'
    elif result >=60 and reports <=69:
      asess = 'C'
    else:
      asess = 'D'

    print(asess)



