
def compay(hours, code):
  if code == "L":
    rate = 25 
  elif code == "A":
    rate = 30 
  else:
    rate = 50 

  if hours <= 40:
    pay = hours * rate
  else:
    pay = hours * rate * 1.5

  return pay




affirm = input ("Run program(Y/N)?: ")
c = 0

while affirm == "Y":
  lname=input("Enter your last name: ")
  code = input("Enter your job code(L/A/J): ")
  hours = float(input("Enter the number of hours worked: "))
  grosspay = compay(hours, code)
  print("Last name: ", lname)
  print ("Gross pay: ", grosspay)
  c += grosspay
  affirm = input ("Run program(Y/N)?: ")

print ("Total gross pay: ", c)