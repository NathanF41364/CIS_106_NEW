#Prompt the user to repeatedly to do the program( input (Yes or No)). If they response Yes go into the loop and prompt the user for last name and miles from downtown Chicago. Write a function to compute the train ticket price. Pass to the function the miles from down town Chicago and determine the ticket price. Return the ticket price. Sum price of all tickets. 
#Miles from Down Town Chicago			Ticket Price
#30 or more					     $12
#20 to 29					     $10
#10 to 19					     $8
#All others					     $5

#Function Ticket Calculator
def CompTicketCalc(miles):
  if miles >= 30:
    ticket = 12
  elif miles >= 20 and miles <= 29:
    ticket = 10
  elif miles >= 10 and miles <= 19:
    ticket = 8
  else:
    ticket = 5

  return ticket


#
affirm = input("Run the program(y/n): ")
sumprice = 0
while affirm == "y":
  lname = input ("Enter the last name: ")
  miles = float(input("Enter the miles from downtown Chicago: "))
  ticketprice = CompTicketCalc(miles)
  print ("Last name: ", lname)
  print ("Ticket Price: $", format(ticketprice, '<,.2f'))
  sumprice += ticketprice
  affirm = input("Run the program(y/n): ")

print ("Ticket Price Total: $", format(sumprice, '<,.2f'))