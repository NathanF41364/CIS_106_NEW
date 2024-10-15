#Prompt the user to repeatedly to do the program( input (Yes or No)). If they response Yes go into the loop and prompt the user for length, width and height of a room. Write a function to compute the square footage of the room. The function should receive the length, width and height of the room and return square footage (2 x length x width (floor and ceiling) + 2 x length x height (2 of the walls) + 2 x width x height (the other 2 walls). A gallon of paint covers 50 square feet. Compute the number of gallons needed to paint the room (square footage of the room / 50). Display the number of gallons needed. 

#Function CompSqFtCalc
def CompSqFtCalc(length, width, height):
  sqft = (2 * length * width) + (2 * length * height) + (2 * width * height)
  galreq = sqft / 50
  return galreq
#
affirm = input("Run the program(y/n)?: ")
while affirm == "y":
  length = float(input("Enter the length: "))
  width = float(input("Enter the width: "))
  height = float(input("Enter the height: "))
  galreq = CompSqFtCalc(length, width, height)
  print ("Gallons required: ", format(galreq, ',.1f'))
  affirm = input("Run the program(y/n)?: ")