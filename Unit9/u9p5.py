#Prompt the user to repeatedly to do the program( input (Yes or No)). If they response Yes go into the loop and prompt the user for county and market value of a home. Write a function to compute the assessed value. Pass to the function the county and market value. The function will determine the assessed value percent then compute and return the assessed value. (Multiple the market value by assessed value percent. Sum and display all market values and assessed values. 
#County		Assessed Value Percent
#Cook		        0.90
#DuPage		        0.80
#McHenry		        0.75
#Kane		        0.60
#All others		       0.70

# Function Accest Value Calculator
def CompAVCalc(county, market_value):
  if county == "Cook":
    av_percent = 0.90
  elif county == "DuPage":
    av_percent = 0.80
  elif county == "McHenry":
    av_percent = 0.75
  elif county == "Kane":
    av_percent = 0.60
  else:
    av_percent = 0.70
  av_value = market_value * av_percent
  return av_value

#
Affirm = input("Run the program(y/n)?: ")
mvsum =0
avsum =0
while Affirm == "y":
  County = input("Enter the county: ")
  Market_value = float(input("Enter the market value: "))
  av_value = CompAVCalc(County, Market_value)
  print ("Assessed value: ", format(av_value, ',.2f'))
  mvsum += Market_value
  avsum += av_value
  Affirm = input("Run the program(y/n)?: ")

print ("Market value sum: ", format(mvsum, ',.2f'))
print ("Assessed value sum: ", format(avsum, ',.2f'))