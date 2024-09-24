#Input
approve = input("Do you want to continue? (Yes/No) :")
c=0
#Process/Output
while approve == "Yes":
  lname= input("Enter your last name: ")
  exam1= int(input("Enter your exam grade: "))
  exam2= int(input("Enter your exam grade: "))
  avg= (exam1 + exam2) / 2
  print ()
  print ("Last Name: ", lname)
  print ("Average Exam Score: ", str(avg))
  c += 1
  print ("Number of students: ", str(c))
  approve = input("Do you want to continue? (Yes/No) :")