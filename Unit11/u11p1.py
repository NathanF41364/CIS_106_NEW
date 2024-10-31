#Write the code for the following problem. Assign 10 last names to an array. Write a function to display the names. Write another function to display the names in reverse order. 

lnames = ["Smith", "Johnson", "Williams", "Jones", "Brown", "Davis", "Simpson", "Miller", "Wilson", "Anderson"]

#Function to display the names
def CompDisplay():
  for names in lnames:
    print (names)

#Function to display the names in reverse order
def CompReverse():
  for names in reversed(lnames):
    print (names)

names = CompDisplay()
print ()
rev = CompReverse()