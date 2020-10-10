class MenuItem:
    
  def info(self):
    print(self.name + ':¥' + str(self.price))

  def total_price(self,count):
    get_total_price = self.price * count
    return get_total_price

menu_item1 = MenuItem()
menu_item1.name = 'サンドイッチ'
menu_item1.price = 500


menu_item1.info()


menu_item2 = MenuItem()
menu_item2.name = 'チョコケーキ'
menu_item2.price = 400


menu_item2.info()

result = menu_item1.total_price(4)
print('合計:' + str(result))