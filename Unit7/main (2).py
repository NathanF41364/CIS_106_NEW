f = open("ps8p5t.txt", "r")
c = 0
totp = 0
lname= str(f.readline().rstrip('\n'))

while lname != "":
  dcode = (f.readline().rstrip('\n'))
  credits = float(f.readline())
  if dcode == "I":
    cost = 250.00
  else:
    cost = 500.00
  tuition = float(credits) * float(cost)
  totp += tuition
  c += 1
  #display
  print ("Last name: ", lname)
  print ("Credits taken: ", credits)
  print ("Tuition owed: ", tuition)

print ("Total tuition owed: ", totp)
print ("Number of students: ", c)