class MenuItem:
    
  def info(self):
    print(self.name + ':¥' + str(self.price))

  def total_price(self,count):
    get_total_price = self.price * count
    return get_total_price


  def __init__(self,name,price ):
    self.name = name
    self.price = price
