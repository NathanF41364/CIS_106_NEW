f = open("ps8p3t.txt", "r")
bonus_tot = 0
lname = str(f.readline().rstrip('\n'))


while lname != "":
  salary = float(f.readline())
  if salary >= 100000.00:
    bonus = 0.2
  elif salary >=50000 and salary < 100000:
    bonus = 0.15
  else:
    bonus = 0.1
  bonus_amnt= salary * bonus
  #display
  print ("Employee last name: ", lname)
  print ("Employee salary: ",salary)
  print ("Employee bonus: ", bonus_amnt)
  bonus_tot += bonus_amnt
  lname = str(f.readline().rstrip('\n'))

print ("Bonus Total: ", bonus_tot)