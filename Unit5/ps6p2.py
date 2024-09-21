#Input
prt = int(input("Enter the part number: "))
qty = int(input("Enter the quantity: "))

#Process
if prt == 10 or prt == 55:
  unit_c = 1.00
elif prt == 99:
  unit_c = 2.00
elif prt == 80 or prt == 70:
  unit_c = 3.00
else:
  unit_c = 5.00

#Output
print ("Part Number: ", str(prt))
print ("Cost per Unit: ", str(unit_c))
print ("Total Cost: ", str(qty * unit_c))