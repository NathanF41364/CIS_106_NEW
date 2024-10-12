def compbavg(hits, bats):
  avg = float(hits) / float(bats)
  return avg

affrim = input("Compute bat average(Y/N)?: ")
c=0
while affrim == "Y":
  lname = input("Enter last name: ")
  hits = float(input("Enter number of hits: "))
  bats = float(input("Enter number of at bats: "))
  avg = compbavg(hits, bats)
  print("Last name: ", lname)
  print("Batting average: ", avg)
  c+= 1
  affrim = input("Compute bat average(Y/N)?: ")

print ("Number of players entered: ", c)