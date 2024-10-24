#Enter the student’s last name and 3 exam scores. Use a function to compute the average and total points. This functions should return both total points and exam score. Display student last name, total points and average exam score. 

#Function
def Compscore(lname, exam1, exam2, exam3):
  total = exam1 + exam2 + exam3
  avg = total / 3
  return total, avg


lname= input("Enter the students last name: ")
exam1= int(input("Enter the students exam score: "))
exam2= int(input("Enter the students exam score: "))
exam3= int(input("Enter the students exam score: "))
total, avg= Compscore(lname, exam1, exam2, exam3)
print ()
print ("Last Name: ", lname)
print ("Total Points: ", str(total))
print ("Average Exam Score: ", format(str(avg), '.2s'))