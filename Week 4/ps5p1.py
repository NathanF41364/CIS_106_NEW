#Input
qty=int(input("Enter the quantity of the item: "))

#Process
if qty >= 1000:
  price= float(qty * 3.00)
  unit_p=float(3.00)
else:
  price= float(qty * 5.00)
  unit_p=float(5.00)

tax = float(price * 0.07)
total = float(price + tax)

#Output
print ("Stats")
print ("Quantity: ", str(qty))
print ("Unit Price: ", str(unit_p))
print ("Extended Price: ", str(price))
print ("Tax: ", str(tax))
print ( "Total: ", str(total))