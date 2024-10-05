f = open("ps8p5t.txt", "r")
c = 0
totp = 0
lname = str(f.readline().rstrip('\n'))

while lname != "":
    dcode = (f.readline().rstrip('\n'))
    credits = f.readline().rstrip('\n')
    if dcode == "I":
        cost = 250.00
    else:
        cost = 500.00

    tuition = float(credits) * float(cost)
    totp += tuition
    c += 1

    # Output
    print("Last name: ", lname)
    print("Credits taken: ", credits)
    print("Tuition owed: ", tuition)

    lname = str(f.readline().rstrip('\n'))

# Final totals
print()
print("Total tuition owed: ", totp)
print("Number of students: ", c)
