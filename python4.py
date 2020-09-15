def calc_tax(price,tax_rate):
  tax_inc_price = price * (1 +tax_rate)

  return tax_inc_price


print(calc_tax(2000,0.08),"円")
print(calc_tax(2000,0.1),"円")
