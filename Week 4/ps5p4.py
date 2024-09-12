#Input
name = input("Enter the name of the appliance: ")
cost = float(input("Enter the cost of the appliance: "))

#Process
if cost > 1000:
  cost_w = cost * 0.1
else:
  cost_w = cost * 0.05

total = cost + cost_w

#Output
print ("Stats")
print ("Name of appliance: ", name)
print ("Cost of appliance: ", str(cost))
print ("Cost of warranty: ", str(cost_w))
print ("Total cost: ", str(total))