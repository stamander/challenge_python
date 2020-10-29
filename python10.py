day,buy_price,sell_price = list(map(int, input().split())) 





stock = [int(input()) for i in range(day)]

have_stock = 0
benefit = 0


for stock_price in stock:
  if stock_price < buy_price:
    have_stock+=1
    benefit-=buy_price
  elif stock_price > sell_price:
    have_stock=0
    benefit+=have_stock*sell_price
  elif buy_price <= stock_price >= sell_price:
    have_stock = have_stock
    benefit = benefit

  


print(benefit)





