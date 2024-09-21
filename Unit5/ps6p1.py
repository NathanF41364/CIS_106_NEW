#Input
qty = int(input("Enter the quantity of widgets: "))

#Process
if qty > 10000:
  price = 10
elif qty >= 5000 and qty <= 10000:
  price = 20
else:
  price = 30

price_ext = qty * price
tax = price_ext * 0.07
total = price_ext + tax

#Output
print ("The extended price is: ", str(price_ext))
print ("The tax is: ", str(tax))
print ("The total is: ", total)