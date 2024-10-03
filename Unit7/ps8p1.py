#Input
pamnt = float(input("Enter the payment amount: "))
irate = float(input("Enter the interest rate: "))
itot = 0
#Process
iannual = pamnt * irate
eb= pamnt + iannual
print ("Year    Starting Balance    Ending Balance")
for count in range (1,6):
  print (count,"     ",pamnt,"            ",eb)
  pamnt = eb
  eb = pamnt + iannual
  itot += (eb - pamnt)

print ("Total interest earned: $",itot)