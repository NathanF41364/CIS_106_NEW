#Write the code for the following problem. Add another array to problem 1 above. This array should contain exam score for the respective students. That is, the first name goes with the first score etc. These are called parallel arrays. Also modify the display functions to include exam score array in addition to the last name array. 


lnames = ["Smith", "Johnson", "Williams", "Jones", "Brown", "Davis", "Simpson", "Miller", "Wilson", "Anderson"]
exam_scores = [85, 92, 78, 90, 88, 95, 89, 91, 87, 94]

#Function
def CompParallel(lnames, exam_scores):
  for i in range(len(lnames)):
    print (lnames[i], exam_scores[i])


#Display
disp = CompParallel(lnames, exam_scores)