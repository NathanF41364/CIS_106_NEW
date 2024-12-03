# Create a program that asks the user for a line of text. Then ask the user for the number of characters to print in each line, the number of lines to be printed, and a scroll direction, right or left. Using the given line of text, duplicate the text as needed to fill the given number of characters per line. Then print the requested number of lines, shifting the entire line's content by one character, left or right, each time the line is printed. The first or last character will be shifted / appended to the other end of the string. For example, if shifting the line to the left:
#     Repeat this. Repeat this. 
#     epeat this. Repeat this. R
#     peat this. Repeat this. Re
# Or if shifting the line to the right:
#     Repeat this. Repeat this. 
#      Repeat this. Repeat this.
#     . Repeat this. Repeat this


#Functions
def main():
    #Input
    text = input("Enter a line of text: ")
    char_num = int(input("Enter the number of characters to print in each line: "))
    line_num = int(input("Enter the number of lines to be printed: "))
    direction = input("Enter the scroll direction (right or left): ")
    #Process
    repeated_text = text_repetition(text, char_num)

    for i in range(line_num):
        print (repeated_text)
        repeated_text = shift_direction(repeated_text, direction)
    
    
    

def text_repetition(text, char_num):
    reps_needed = (char_num // len(text))+1
    repeated_text = (text * reps_needed)[:char_num]
    return repeated_text

def shift_direction(repeated_text, direction):
    if direction == "left":
        return repeated_text[1:] + repeated_text[0]
    elif direction == "right":
        return repeated_text[-1] + repeated_text[:-1]
    else:
        return "Invalid Input"
    



#main
main()