#Starting with the employee class you created in the previous assignment, create a manager class. This class should use the previously created employee class as the base class and make a derived class called manager. This class should include a long term bonus method that compute the long term bonus to be 40% of their salary. Create a program to instantiate the new class and show that it works. 

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

class Manager(Employee):
    def __init__(self, first, last, pay, bonus_rate):
        super().__init__(first, last, pay, bonus_rate)

    def long_term_bonus(self):
        lt_bonus = self.pay * 0.4
        return lt_bonus        


emp1 = Employee("Corey", "Schafer", 50000, 0.1)
emp2 = Employee("Test", "User", 60000, 0.2)

mng1 = Manager("John", "McArthur", 100000, 0.1)
print (mng1.long_term_bonus())