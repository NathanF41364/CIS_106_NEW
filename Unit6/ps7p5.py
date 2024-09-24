#Input
approve = input("Do you want to continue? (Yes/No) :")
disc_sum=0
total=0
#Process/Output
if approve == "Yes":
 while approve == "Yes":
   qty = int(input("Enter the quantity of items: "))
   price = int(input("Enter the price per item: "))
   price_ext= qty * price
   if price_ext > 10000:
     disc_amnt = price_ext * 0.25
   else:
     disc_amnt = price_ext * 0.10
   print ("Extended Price: ", str(price_ext))
   print ("Discount Amount: ", str(disc_amnt))
   print ("Total: ", str(price_ext - disc_amnt))
   disc_sum += disc_amnt
   print ()
   approve = input("Do you want to continue? (Yes/No): ")
 print("Discount Total: ", str(disc_sum))
else:
  print ()
  print ("Why did you even run the program!?")
  print ("You are such a waste of time")
  print ("If you were a computer, I would unplug you")
  print (">:(")