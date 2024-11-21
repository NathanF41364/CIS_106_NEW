#Create a car class. This should have methods for make, model, sticker price and discount price (90% of sticker price). Then create a derived class called sport. Inherit the car class but add options methods. Set the option to Y to include the option in the updated price method. See table below. Define a method for each option.

#Option (method)	Option Price
#SportWheels		1000.00
#SportEngine		3000.00
#SportInterior		2000.00

#For each method set to Y add the amounts to the updated price and display using a method called price with options. 
#Write a program to instantiate the object and show that it works. 

#Class
## CAR
class Car:

  def __init__(self, make, model, sticker_price):
    self.make = make
    self.model = model
    self.sticker_price = sticker_price
    

  def display(self):
    print(self.make, self.model)

  def sticker_price_display(self):
    print(self.sticker_price)

  def discount_price_display(self):
    print (self.sticker_price * 0.9)
## SPORT
class Sport(Car):

  def __init__(self, make, model, sticker_price, options=None):
    super().__init__(make, model, sticker_price)
    self.options = options
    if options is None:
      self.options = []
    else:
      self.options = options

  def add_options(self, opt):
    if opt not in self.options:
      self.options.append(opt)

  def remove_options(self, opt):
    if opt in self.options:
      self.options.remove(opt)
    

  def print_options(self):
    for opt in self.options:
      print(opt)

  def price_w_options(self):
    if 'SportWheels' in self.options:
      self.sticker_price += 1000.00
    if 'SportEngine' in self.options:
      self.sticker_price += 3000.00
    if 'SportInterior' in self.options:
      self.sticker_price += 2000.00
    print(self.sticker_price)
      
    




#Main
print('Class Car Example: Displaying Make, Model, Sticker Price, and Discount Price')
print()
car1 = Car("Nissan", "Silvia", 50000)
car1.display()
car1.discount_price_display()
car1.sticker_price_display()
print()
print()
print()
print()
print('Subclass Sport Example: Displaying make and model through the car class, adding and removing options, displaying options, and displaying the price with options')
print()
sport1 = Sport("Nissan", "Silvia", 50000, ["SportWheels", "SportEngine"])
sport1.display()

sport1.print_options()
sport1.add_options("SportInterior")
sport1.remove_options("SportWheels")
sport1.price_w_options()