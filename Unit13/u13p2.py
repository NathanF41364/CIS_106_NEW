#Create a student class. This class should consist of student first name, student last name, district code (I or O) and enrolled credits. Create a method to compute tuition owed. Tuition owed should be enrolled credits times $250.00 per credit hour for in district students (district code of I) and or times $500.00 per credit hour for out of district students (district code of anything other than I). Test the class by instantiating the object and adding data. 

#Class
class Student:

  def __init__(self, first, last, district_code, credits):
    self.first = first
    self.last = last
    self.district_code = district_code # I or O
    self.credits = credits

  def tuition(self):
    if self.district_code == "I":
      tuition = self.credits * 250.00
    else:
      tuition = self.credits * 500.00

    return tuition

# Students
student1 = Student("John", "Doe", "I", 12)
student2 = Student("Jane", "Doe", "O", 10)
student3 = Student("Jim", "Doe", "I", 8)

# Output
print ("Student 1 Tuition: ",format(student1.tuition(), '.2f'))
print ("Student 2 Tuition: ",format(student2.tuition(), '.2f'))
print ("Student 3 Tuition: ",format(student3.tuition(), '.2f'))