#Input
item = str(input("Enter item A or B: "))
qty = int(input("Enter quantity: "))

#Process
if item == "A":
  price_u = float(10.00)
else:
  price_u = float(20.00)

price_e = float(qty) * price_u

#Output
print(" ")
print ("Stats")
print ("Item: ", item)
print ("Unit Price: ", str(price_u))
print ("Extended Price: ", str(price_e))