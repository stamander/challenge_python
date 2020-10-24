money,buy_stock,sell_stock = [int(input()) for i in range(3)]

total_buy = money/buy_stock

total_sell = total_buy * sell_stock


print(total_buy,total_sell)