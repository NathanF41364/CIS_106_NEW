#Allow the user to enter quantity of an item and unit price. Write a function to compute total (qty * unit price) and tax (7% of total). Demonstrate your knowledge of global variables by making total and tax global in scope. Display total and tax in main. 

#Function
def CompPrice(qty, up):
  global total
  total = qty * up
  global tax
  tax = total * 0.07
  

qtp = int(input("Enter the quantity of the item: "))
up = float(input("Enter the unit price of the item: "))
CompPrice(qtp, up)
print()
print ("Total: ", format(total, ',.2f'))
print ("Tax: ", format(tax, ',.2f'))