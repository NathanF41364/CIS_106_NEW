#Write the code for the following problem. The data to load is lastname and score. You can do this from a file.  Add a function to problem to display the last name and highest, last name and lowest. Hint: for highest initialize a variable to 0 (high_var). If the array value is higher than the high_var then set high_var to the array value and set high_index to the position of the array. Proceed through the array until you get to the end. Do the same for finding the lowest using low_var set to 999 (higher than the highest value). 


f = open("u11t3.txt", "r")

lname = []
salary = []

name = f.readline().strip()


while name != "":
    lname.append(name)
    s = float(f.readline().strip())  
    salary.append(s)
    name = f.readline().strip()
f.close()

# Function to compare high and low salaries
def CompHiLow(lname, salary):
    l = len(lname)
    hisal = -1.0
    lowsal = 99999.99
    high_index = 0
    low_index = 0

    for y in range(l):
        if float(salary[y]) > hisal:
            hisal = salary[y]
            high_index = y

        if float(salary[y]) < lowsal:
            lowsal = salary[y]
            low_index = y

    print("Highest Salary: ", lname[high_index], salary[high_index])
    print("Lowest Salary: ", lname[low_index], salary[low_index])

# Display
CompHiLow(lname, salary)

