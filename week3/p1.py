#Input
sts = input(str("Enter the stock tier symbol: "))
num_shares = float(input("Enter the number of shares: "))
cost_shares = float(input("Enter the cost per share: "))

#Process
num_invest = num_shares * cost_shares

#Output
print ("Amount invested: ", num_invest)