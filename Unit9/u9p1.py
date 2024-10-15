#Prompt the user to repeatedly to do the program( input (Yes or No)). If they respond Yes, go into the loop and prompt them for last name, month and sales. Write a function to compute next month’s forecast. Pass to the function month and sales. Determine the forecast percent (see below) and compute next month’s sales to be sales x (1+forecast percent). Return next month’s sales and display the value. 
#Month			Forecast Percent
#Jan, Feb, Mar			0.10
#Apr, May, Jun			0.15
#Jul, Aug, Sep			0.20
#Oct, Nov, Dec			0.25

affirm = input("Do you wish to run the program(y/n)? :")
#function: CompForcastCalc
def CompForcastCalc(month, sales):
  if month == "Jan" or month == "Feb" or month == "Mar":
    forecast_percent = 0.10
  elif month == "Apr" or month == "May" or month == "Jun":
    forecast_percent = 0.15
  elif month == "Jul" or month == "Aug" or month == "Sep":
    forecast_percent = 0.20
  else:
    forecast_percent = 0.25

  nms = sales * (1 + forecast_percent)
  return nms
#
while affirm == "y":
  lname = input("Enter the last name: ")
  month = input("Enter the month: ")
  sales = float(input("Enter the sales: "))
  nms = CompForcastCalc(month, sales)
  print("Next month's sales: $",format(nms, ',.2f'))
  affirm = input("Do you wish to run the program(y/n)? :")
  