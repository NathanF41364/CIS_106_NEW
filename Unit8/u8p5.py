def comptuition(credithrs, code):
  if code == "I":
      tuition = credithrs * 250
  elif code == "O":
      tuition = credithrs * 550
  return tuition

affirm = input("Run Program(Y/N)?: ")
c = 0

while affirm == "Y":
  lname = input("Enter your last name: ")
  credithrs = int(input("Enter your credit hours: ")) 
  code = input("Enter your district code(I/O): ")
  tuition = comptuition(credithrs, code)
  print("Last name: ", lname)
  print("Tuition owed: ", tuition)
  c += tuition
  affirm = input("Run Program(Y/N)?: ")

print("Total tuition owed: ", c)
