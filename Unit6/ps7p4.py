#Input
approve = input("Do you want to continue? (Yes/No) :")
c=0
total=0
#Process/Output
if approve == "Yes":
  while approve == "Yes":
    lname= input("Enter your last name: ")
    hrs= int(input("Enter the amount of hours that you worked: "))
    rate= int(input("Enter your pay rate: "))
    if hrs <= 40:
      gross = hrs * rate
    else:
      gross = (40 * rate) + ((hrs - 40) * (rate * 1.5))
    print ("Last Name: ", lname)
    print ("Gross Pay: ", str(gross))
    c+=1
    total +=gross
    print()
    approve = input("Do you want to continue? (Yes/No) :")
  print ("Total Employees: ", str(c))
  print ("Total Payroll: ", str(total))
  print ("Average Gross Pay: ", str(total/c))
else:
  print ()
  print ("Why did you even run the program!?")
  print ("You are such a waste of time")
  print ("If you were a computer, I would unplug you")
  print (">:(")

