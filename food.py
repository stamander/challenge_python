# fromとimportを用いて、MenuItemクラスを読み込んでください
from menu_item import MenuItem

# MenuItemクラスを継承して、Foodクラスを定義してください
class Food(MenuItem):
    def info(self):
      return self.name + ': ¥' + str(self.price) + ' (' + str(self.calorie) + 'kcal)'

    def calorie_info(self):
      print(str(self.calorie) + 'kcalです')
