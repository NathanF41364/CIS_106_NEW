#Input
qty = float(input("Enter the number of books: "))
cost = float(input("Enter the cost per book: "))

#Process
total = qty * cost
if total >= 50:
  ship = float(0)
else:
  ship = float(25)

#Output
print ("Total: ", str(total))
print ("Shipping: ", str(ship))