#Create a program that asks the user for a line of text. Use string functions/methods to delete leading, trailing, and duplicate spaces, and then print the line of text backwards. For example:
#      the   cat   in   the   hat  
#    tah eht ni tac eht
#Use separate subroutines/functions/methods to implement input, each type of processing, and output. Avoid global variables by passing parameters and returning results.

#Function to deleat spacing
def CompDelSpace(text):
  split_text = text.split()
  clean_text = " ".join(split_text)
  final_text = CompReverse(clean_text)
  print(final_text)
  
  
def CompReverse(clean_text):
  final_text = clean_text[::-1]
  return final_text


text = str(input("Enter a line of text: "))
CompDelSpace(text)