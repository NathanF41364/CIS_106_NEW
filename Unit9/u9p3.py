#Prompt the user to repeatedly to do the program (input (Yes or No)). If they response Yes go into the loop and prompt the user for make, model, electric vehicle code (Y or N) and MSRP (sticker price) of an automobile. Write a function to compute the out the door price. Pass to the function the MSRP, make, model and electric vehicle code. Determine the percent off the MSRP then compute the new MSRP and finally add 7% sales tax to the total. Return and display the total. Also sum all MSRP’s and sum of all sales price of the cars (MSRP – discount + tax).
#To determine percent off MSRP			Percent off MSRP
#Honda Accord					      0.10
#Toyota Rav4					      0.15
#All electric vehicles				      0.30
#All other vehicles				      0.05

# Function CompODP
def CompODP(MSRP, make, model, electric):
  if make == "Honda" and model == "Accord":
    percent = 0.10
  elif make == "Toyota" and model == "Rav4":
    percent = 0.15
  elif electric == "Y":
    percent = 0.30
  else:
    percent = 0.05
  newMSRP = MSRP - (MSRP * percent)
  total = newMSRP + (newMSRP * 0.07)
  return total

#
totalsum = 0
msrpsum = 0
#
affirm = input("Run the program(y/n)? :")
while affirm == "y":
  make = input("Enter the make: ")
  model = input("Enter the model: ")
  ev_code = input("Enter the electric vehicle code(y/n): ")
  msrp = float(input("Enter the MSRP: "))
  total = CompODP(msrp, make, model, ev_code)
  print ("The out the door price is: $", format(total, ',.2f'))
  totalsum += total
  msrpsum += msrp
  affirm = input("Run the program(y/n)? :")
#
print ("The total sum of all MSRP's is: $", format(msrpsum, ',.2f'))
print ("The total sum of all sales price is: $", format(totalsum, '.2f'))