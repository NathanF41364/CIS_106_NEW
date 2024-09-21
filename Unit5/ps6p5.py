#Input
lname = input("Enter the employee's last name: ")
salary = int(input("Enter the employee's salary: "))
level = int(input("Enter the employee's job level: "))

#Process
if level >= 10:
  rate = 0.25
elif level >= 5 and level <= 9:
  rate = 0.2
else:
  rate = 0.1

bonus = int(salary * rate)

#Output
print ("")
print ("Employee: ", lname)
print ("Bonus: ", str(bonus))