#Starting with the employee class you created in the previous assignment, create a manager class. This class should use the previously created employee class as the base class and make a derived class called manager. This class should include a long term bonus method that computes the long term bonus to be 40% of their salary. Create a program to instantiate the new class and show that it works. 
#Create a derived class called Executive. 
#Add a method called ExecutiveBonus computed to be 200% of their annual salary. 
#Override the long term bonus method to be 50% of their annual salary. 
#Instantiate and test your object. 

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
        print (lt_bonus)   

class Executive(Manager):
    def __init__(self, first, last, pay, bonus_rate):
        super().__init__(first, last, pay, bonus_rate)

    def Exec_Bonus(self):
      EB = self.pay * 2
      print (EB)

    def long_term_bonus(self):
      lt_bonus = self.pay * 0.50
      print (lt_bonus)


emp1 = Employee("Corey", "Schafer", 50000, 0.1)
emp2 = Employee("Test", "User", 60000, 0.2)

mng1 = Manager("John", "McArthur", 100000, 0.1)
print (mng1.long_term_bonus())

exec1 = Executive("Nicolas", "Cage", 200000, 0.1)
exec1.Exec_Bonus()
exec1.long_term_bonus()