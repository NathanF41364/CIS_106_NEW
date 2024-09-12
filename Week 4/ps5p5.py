#Input
name_l = input("Enter last name: ")
dep_num = int(input("Enter the number of dependents: "))
gross = float(input("Enter your gross income: "))

#Process
gross_adj = gross - dep_num * 12000
if gross_adj > 50000:
  tax_r = 0.2
else:
  tax_r = 0.1

tax_i = gross_adj * tax_r

if tax_i < 0:
  tax_i=100

#Output
print ("Stats")
print ("Last name: ", name_l)
print ("Gross income: ", str(gross))
print ("Number of dependents: ", str(dep_num))
print ("Adjusted gross income: ", str(gross_adj))
print ("Income Tax: ", str(tax_i))