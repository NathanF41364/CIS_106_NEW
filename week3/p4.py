#Input
make = str(input("Enter the make of the car: "))
model = str(input("Enter the model of the car: "))
msrp = float(input("Enter the MSRP: "))
discount_dec = float(input("Enter the discount percentage in decimal form: "))

#Process
amount_off = msrp * discount_dec
discount_price = msrp - amount_off
discount_per = discount_dec * 100

#Output
print ("Make: ", make)
print ("Model: ", model)
print ("MSRP: ", msrp)
print (discount_per, "% off")
print ("Amount off: ", amount_off)
print ("Discounted Price: ", discount_price)