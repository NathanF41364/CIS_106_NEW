#The input consists of quantity, price and discount rate. Use a function to compute the discount amount and discounted price. Then display these values in main along with the quantity and price. (The function should return both discount amount and discounted price). 


#Function
def CompDiscount(qty, price, discount):
  disc_amt = qty * price * discount
  disc_price = qty * price - disc_amt
  return disc_amt, disc_price

qty = int(input("Enter the quantity: "))
price = float(input("Enter the price: "))
discount = float(input("Enter the discount rate: "))
disc_amt, disc_price = CompDiscount(qty, price, discount)
print ("Quantity: ", qty)
print ("Price: ", price)
print ("Discount Amount: ", disc_amt)
print ("Discounted Price: ", disc_price)