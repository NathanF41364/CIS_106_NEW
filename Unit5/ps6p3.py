#Input
cd_pa = int(input("Enter the principle amount of a CD: "))
cd_m = int(input("Enter the year to maturity of the CD: "))

#Process
if cd_pa > 100000 and cd_m == 5:
  rate_i = 0.06
elif cd_pa >= 50000 and cd_pa <= 100000 and cd_m == 10:
  rate_i = 0.05
elif  cd_pa >= 50000 and cd_pa <= 100000 and cd_m == 5:
  rate_i = 0.04
else:
  rate_i = 0.02

amount_i = float(cd_pa * rate_i)

#Output
print ("Principle Amount :", str(cd_pa))
print ("Interest Rate: ", str(rate_i))
print ("Interest Amount for the First Year: ", str(amount_i))