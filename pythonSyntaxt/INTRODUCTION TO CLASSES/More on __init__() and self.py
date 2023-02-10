class Animal(object):
  """Makes cute animals."""
  is_alive = True
  def __init__(self, name, age):
    self.name = name
    self.age = age

zebra = Animal("Jeffrey", 2)
giraffe = Animal("Bruce", 1)
panda = Animal("Chad", 7)

print zebra.name, zebra.age, zebra.is_alive
print giraffe.name, giraffe.age, giraffe.is_alive
print panda.name, panda.age, panda.is_alive



# A mothodical Avarage

class Animal(object):
  """Makes cute animals."""
  is_alive = True
  def __init__(self, name, age):
    self.name = name
    self.age = age
    
# They're Multiplying!

class Animal(object):
  """Makes cute animals."""
  is_alive = True
  def __init__(self, name, age):
    self.name = name
    self.age = age
  # Add your method here!



# It's Not All Animals and Fruits
class ShoppingCart(object):
  """Creates shopping cart objects
  for users of our fine website."""
  items_in_cart = {}
  def __init__(self, customer_name):
    self.customer_name = customer_name

  def add_item(self, product, price):
    """Add product to the cart."""
    if not product in self.items_in_cart:
      self.items_in_cart[product] = price
      print product + " added."
    else:
      print product + " is already in the cart."

  def remove_item(self, product):
    """Remove product from the cart."""
    if product in self.items_in_cart:
      del self.items_in_cart[product]
      print product + " removed."
    else:
      print product + " is not in the cart."



# Warning: Here Be Dragons
class Customer(object):
  """Produces objects that represent customers."""
  def __init__(self, customer_id):
    self.customer_id = customer_id

  def display_cart(self):
    print "I'm a string that stands in for the contents of your shopping cart!"

class ReturningCustomer(Customer):
  """For customers of the repeat variety."""
  def display_order_history(self):
    print "I'm a string that stands in for your order history!"

monty_python = ReturningCustomer("ID: 12345")
monty_python.display_cart()
monty_python.display_order_history()



# inheritance syntext
class Shape(object):
  """Makes shapes!"""
  def __init__(self, number_of_sides):
    self.number_of_sides = number_of_sides

# Add your Triangle class below!
class Tringle(Shape):
  def __init__(self,side1,side2,side3):
    self.side1 = side1
    self.side2 = side2
    self.side3 = side3
    
    
# This Looks Like a Job For...
class Employee(object):
  """Models real-life employees!"""
  def __init__(self, employee_name):
    self.employee_name = employee_name

  def calculate_wage(self, hours):
    self.hours = hours
    return hours * 20.00

# Add your code below!
class PartTimeEmployee(Employee):
  def calculate_wage(self, hours):
    self.hours = hours
    return hours * 12.00
  
  def full_time_wage(self, hours):
    return super(PartTimeEmployee, self).calculate_wage(hours)

milton = PartTimeEmployee('Milton')
print milton.full_time_wage(10)



# Class basic
class Triangle(object):
  def __init__(self, angle1, angle2, angle3):
    self.angle1 = angle1
    self.angle2 = angle2
    self.angle3 = angle3
    
# Class it up
class Triangle(object):
  number_of_sides = 3
  def __init__(self, angle1, angle2, angle3):
    self.angle1 = angle1
    self.angle2 = angle2
    self.angle3 = angle3
    
  def check_angles(self):
    if (self.angle1 + self.angle2 + self.angle3) == 180:
      return True
    else:
      return False
  

# Instantiate an Object
class Triangle(object):
  number_of_sides = 3
  def __init__(self, angle1, angle2, angle3):
    self.angle1 = angle1
    self.angle2 = angle2
    self.angle3 = angle3
    
  def check_angles(self):
    if (self.angle1 + self.angle2 + self.angle3) == 180:
      return True
    else:
      return False
    
my_triangle = Triangle(30, 60, 90)
print my_triangle.number_of_sides
print my_triangle.check_angles()


# Inheritance
class Triangle(object):
  number_of_sides = 3
  def __init__(self, angle1, angle2, angle3):
    self.angle1 = angle1
    self.angle2 = angle2
    self.angle3 = angle3
    
  def check_angles(self):
    if (self.angle1 + self.angle2 + self.angle3) == 180:
      return True
    else:
      return False
    
class Equilateral(Triangle):
  angle = 60
  def __init__(self):
    self.angle1 = self.angle
    self.angle2 = self.angle
    self.angle3 = self.angle
    
    
# modifying member variables
class Car(object):
  condition = "new"
  def __init__(self, model, color, mpg):
    self.model = model
    self.color = color
    self.mpg   = mpg
   
  def display_car(self):
    print "This is a %s %s with %s MPG." % (self.color, self.model, str(self.mpg))
 
  def drive_car(self):
    self.condition  = "used"

my_car = Car("DeLorean", "silver", 88)

print(my_car.condition)
drive_car()
print(mycondition)


# Inheritance
class Car(object):
  condition = "new"
  def __init__(self, model, color, mpg):
    self.model = model
    self.color = color
    self.mpg   = mpg
   
  def display_car(self):
    print "This is a %s %s with %s MPG." % (self.color, self.model, str(self.mpg))
 
  def drive_car(self):
    self.condition  = "used"

my_car = Car("DeLorean", "silver", 88)

print(my_car.condition)
drive_car()
print(mycondition)
class ElecricCar(Car):
  def __init__(battery_type):



# Overriding methods
class Car(object):
  condition = "new"
  def __init__(self, model, color, mpg):
    self.model = model
    self.color = color
    self.mpg   = mpg
   
  def display_car(self):
    print "This is a %s %s with %s MPG." % (self.color, self.model, str(self.mpg))
    
  def drive_car(self):
    self.condition = "used"
    
class ElectricCar(Car):
  def __init__(self, model, color, mpg, battery_type):
    self.model = model
    self.color = color
    self.mpg   = mpg
    self.battery_type = battery_type
    
  def drive_car(self):
    self.condition = "like new"

my_car = ElectricCar("DeLorean", "silver", 88, "molten salt")

print my_car.condition
my_car.drive_car()
print my_car.condition



# Building useful classes
class Point3D(object):
  def __init__(self):
    self.x = x
    self.y = y
    self.z = z
  def __repr__():
    return "(%d, %d, %d)" % (self.x, self.y, self.z)


# Bank account project 
class BankAccount(object):
  
  balance = 0
  
  def __init__(self, name):
    self.name = name
    
  def __repr__(self):
    return "Account holder: %s; Balance: $%.2f" % (self.name, self.balance)
  
  def show_balance(self):
    print "Balance: $%.2f" % self.balance
    
  def deposit(self, amount):
    if amount <= 0:
      print "Deposit must be a positive amount"
      return
    print "Deposit amount: $%.2f" % amount
    self.balance += amount
    self.show_balance()
    
  def withdraw(self, amount):
    if amount > self.balance:
      print "Insufficient funds to withdraw $%.2f;" % amount,
      self.show_balance()
      return
    print "Withdrawal amount: $%.2f" % amount
    self.balance -= amount
    self.show_balance()

my_account = BankAccount("Arthur Gordon-Wright")
print my_account
my_account.show_balance()
my_account.deposit(2000)
my_account.deposit(0)
my_account.withdraw(1000)
print my_account
my_account.withdraw(1001)



# 