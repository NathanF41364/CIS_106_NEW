#Create a program that asks the user for a single line of text containing a first name and last name, such as Firstname Lastname. Use string functions/methods to parse the line and print out the name in the form last name, first initial, such as Lastname, F. Include a trailing period after the first initial. Handle invalid input errors, such as extra spaces or missing name parts.

#Input
names = str(input("Enter your first and last name: "))

#Process
test = names.split()
test_len = len(test)
if test_len == 2:
  fname, lname = names.split()
  finitial = fname[0]
  finit_upper = finitial.upper()
  ffinal = "".join([finit_upper, "."])
  lname_strip = lname[0]
  lname_remain = lname[1:]
  lname_upper = lname_strip.upper()
  lname_final = "".join([lname_upper, lname_remain])
  print (lname_final, ffinal)
else: 
  print ("Invalid input")