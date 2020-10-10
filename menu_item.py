class MenuItem:
  def __init__(self,name,price ):
    self.name = name
    self.price = price
    
  def info(self):
    return self.name + ':¥' + str(self.price)

  def total_price(self,count):
    get_total_price = self.price * count
    

    if count >= 3:
      get_total_price *= 0.9

    return round(get_total_price)

