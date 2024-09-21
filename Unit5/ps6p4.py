#Input
qty = int(input("Enter the amount of tickets: "))

#Process
if qty >= 25:
  ppt = 50
elif qty >=10 and qty <= 24:
  ppt = 60
elif qty >= 5 and qty <= 9:
  ppt = 70
else:
  ppt = 75

total = qty * ppt

#Output
print ("Ticket Quantity: ", str(qty))
print ("Price per Ticket: ", str(ppt))
print ("Total: ", str(total))