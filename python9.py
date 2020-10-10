from menu_item import MenuItem





menu_item1 = MenuItem('サンドイッチ',500)
menu_item2 = MenuItem('チョコケーキ',400)

menu_item1.info()

menu_item2.info()

result = menu_item1.total_price(4)
print('合計:' + str(result))