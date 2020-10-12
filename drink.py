# fromとimportを用いて、MenuItemクラスを読み込んでください
from menu_item import MenuItem

# MenuItemクラスを継承して、Drinkクラスを定義してください
class Drink(MenuItem):
    def info(self):
        return self.name + ': ¥' + str(self.price) + ' (' + str(self.amount) + 'mL)'


    def __init__(self,name,price,amount):

        super().__init__(name,price)

        self.amount = amount
