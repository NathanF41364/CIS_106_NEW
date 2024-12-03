#Create a program that asks the user for a line of comma-separated-values. It could be a sequence of test scores, names, or any other values. Use string functions/methods to parse the line and print out each item on a separate line. Remove commas and any leading or trailing spaces from each item when printed.

#Main
def main():
  text = input("Enter a line of comma-seperated-values: ")
  list_text = comp_del_comma(text)
  comp_print_text(list_text)

def comp_del_comma(text):
  list_text = text.split(",")
  return list_text

def comp_print_text(list_text):
  for i in list_text:
    print(i.strip())
  
    




main()