#Enter bowler last name, 3 game scores and handicap. Write a function to compute average score and average score with handicap. Back in main, display last name, average score and average score with handicap. 

#Function
def CompBowl(lname, score1, score2, score3, handicap):
  avg = (score1 + score2 + score3) / 3
  avg_handicap = (score1 + score2 + score3 + handicap) / 3
  return avg, avg_handicap

lname = input("Enter the bowler's last name: ")
score1 = int(input("Enter the first score: "))
score2 = int(input("Enter the second score: "))
score3 = int(input("Enter the third score: "))
handicap = int(input("Enter the handicap: "))
avg, avg_handicap = CompBowl(lname, score1, score2, score3, handicap)
print ()
print ("Last Name: ", lname)
print ("Average Score: ", format(avg, '.2f'))
print ("Average Score with Handicap: ", format(avg_handicap, '.2f'))