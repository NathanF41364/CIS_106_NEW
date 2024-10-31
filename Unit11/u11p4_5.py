#Load list of 10 Player Names and Batting Averages from a file into arrays. (Create your own file with two items: player last name and batting average, i.e. 0.267, 0.300 etc). Write a function to display the arrays. Then use a while loop to repeatedly ask the user for a last name. Write another function to search for the last name in the array and then display last name and batting average when found. 
#Modify 4 above to display a message, “Name not found” when the name is not in the list. 

#For this program, I combined problems 4 and 5 directly into one program.

f = open("u11t4.txt", "r")

#Input
name = f.readline().strip()
lname = []
batting_avg = []
while name != "":
  lname.append(name)
  ba = float(f.readline().strip())
  batting_avg.append(ba)
  name = f.readline().strip()
f.close()

for n in range(len(lname)):
  print (lname[n], batting_avg[n])

#function
def CompSearch(lname, sname):
  l = len(lname)
  sindex = -1
  for y in range (0,l,1):
    if lname[y] == sname:
      sindex = y

  return sindex

#Process
affirm = input("Do you wish to run the program? (y/n)?: ")
while affirm == "y":
  sname = input("Enter the last name of the player you wish to search for: ")
  result = CompSearch(lname, sname)
  if result == -1:
    print ("Name not found")
  else:
    print (lname[result], "has a batting average of", batting_avg[result])
  affirm = input("Do you wish to run the program? (y/n)?: ")