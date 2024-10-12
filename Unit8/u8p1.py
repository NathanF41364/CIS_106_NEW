def compextprice(qty, price):
  extprice = qty * price
  if extprice > 10000:
    disc = extprice * 0.1
  else:
    disc = 0
  return extprice

textprice = 0
affirm = input ("Do you wish to continue(Y/N)?: ")

while affirm == "Y":
  qty = float(input("Enter the quantity: "))
  price = float(input("Enter the price: "))
  extprice = compextprice(qty, price)
  textprice = textprice + extprice
  print ("Extended price is: ", extprice)
  affirm = input ("Do you wish to continue(Y/N)?: ")

print ("Total extended price is: ", textprice)
