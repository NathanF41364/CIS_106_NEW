def compmpg(miles, gallons):
  mpg = float(miles) / float(gallons)
  return mpg

affirm = input ("Compute miles per gallon(Y/N)?: ")
c = 0

while affirm == "Y":
  dcity = input("Enter the destination city: ")
  miles = float(input("Enter the number of miles traveled: "))
  gallons = float(input("Enter the number of gallons used: "))
  mpg = compmpg(miles, gallons)
  c+=1
  print ("Destination city: ", dcity)
  print ("Miles travled: ", miles)
  print ("MPG: ",mpg)
  affirm = input ("Compute miles per gallon(Y/N)?: ")

print ("Number of entries: ",c)