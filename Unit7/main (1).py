f = open("textfiletest.txt", "r")
c = 0
totp_ex = 0
item = str(f.readline().rstrip('\n'))

while item != "":
  qty = float(f.readline())
  price = float(f.readline())
  ep = qty * price
  totp_ex += ep
  c += 1
  print ("Item is: ",item)
  print ("Quantity is: ", str(qty))
  print ("Price is: " , str(price))
  print ("Extended price is: ", str(ep))
  item = str(f.readline().rstrip('\n'))

print ("Total extended price: ", str(totp_ex))
print ("Number of orders: " , str(c))
avg = totp_ex / c
print ("Average order: ", str(avg))