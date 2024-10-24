#Produce a sales report. Input salesperson last name and sales. Write a function that compute commission which is 10% for sales over $100, 000 and 5% for sales at or under $100,000. The function should also computer next year’s target which is 5% of the sales. This function should return both commission and next year’s target. Display salesperson name, commission and next year’s target.  

#Function
def CompSales(lname, sales):
  if sales > 100000:
    com = sales * 0.10
  elif sales <= 100000:
    com = sales * 0.05
  next_y = sales * 0.05
  return com, next_y

lname = input("Enter the salesperson's last name: ")
sales = int(input("Enter the salesperson's sales: "))
com, next_y = CompSales(lname, sales)
print ()
print ("Sales Person: ", lname)
print ("Commission: ", format(com, ',.2f'))
print ("Next Year's Target: ", format(next_y, ' ,.2f'))