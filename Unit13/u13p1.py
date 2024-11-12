#Watch the video on creating a simple class. Create the class in the video and test it to make sure it works. 

#Add a method to the class that accepts a bonus rate for the employee. It should then compute the employee bonus of rate x salary and return this value. Demonstrate this method works by entering a bonus rate and displaying the bonus. 

class Employee:

    def __init__(self, first, last, pay, bonus_rate):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last + "@company.com"
        self.bonus_rate = bonus_rate

    def fullname(self):
        return "{} {}".format(self.first, self.last)

    def bonus(self, bonus_rate):
        bonusr = self.pay * self.bonus_rate
        return bonusr
        

emp1 = Employee("Corey", "Schafer", 50000, 0.1)
emp2 = Employee("Test", "User", 60000, 0.2)

print(emp1.email)
print(emp2.email)
print(emp1.fullname())
print(emp1.bonus(0.10))
