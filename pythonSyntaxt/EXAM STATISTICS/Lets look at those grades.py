grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]
print "Grades:", grades

# Print Those grades

grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]

def print_grades(grade_input):
  for grade in grades:
    print grade


# The sum of the score


grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]

def grades_sum(scores):
  total = 0
  for score in scores: 
    total += score
  return total

print grades_sum(grades)


# Computing the Avrage

grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]

def grades_sum(scores):
  total = 0
  for score in scores: 
    total += score
  return total

print grades_sum(grades)

def grades_average(grades_input):
  sum_of_grades = grades_sum(grades_input)
  average = sum_of_grades / float(len(grades_input))
  return average

print grades_average(grades)

# The Variance

grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]

def print_grades(grades_input):
  for grade in grades_input:
    print grade

def grades_sum(scores):
  total = 0
  for score in scores: 
    total += score
  return total
    
def grades_average(grades_input):
  sum_of_grades = grades_sum(grades_input)
  average = sum_of_grades / float(len(grades_input))
  return average

def grades_variance(scores):
    average = grades_average(scores)
    variance = 0
    for score in scores:
        variance += (average - score) ** 2
    return variance / len(scores)

print grades_variance(grades)

# Standard Derivation

grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]

def print_grades(grades_input):
  for grade in grades_input:
    print grade

def grades_sum(scores):
  total = 0
  for score in scores: 
    total += score
  return total
    
def grades_average(grades_input):
  sum_of_grades = grades_sum(grades_input)
  average = sum_of_grades / float(len(grades_input))
  return average

def grades_variance(grades):
    variance = 0
    for number in grades:
        variance += (grades_average(grades) - number) ** 2
    return variance / len(grades)

def grades_std_deviation(variance):
  return variance ** 0.5

variance = grades_variance(grades)

print grades_std_deviation(variance)



# Review

grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]

def print_grades(grades_input):
  for grade in grades_input:
    print grade

def grades_sum(scores):
  total = 0
  for score in scores: 
    total += score
  return total
    
def grades_average(grades_input):
  sum_of_grades = grades_sum(grades_input)
  average = sum_of_grades / float(len(grades_input))
  return average

def grades_variance(grades):
    variance = 0
    for number in grades:
        variance += (grades_average(grades) - number) ** 2
    return variance / len(grades)

def grades_std_deviation(variance):
  return variance ** 0.5

variance = grades_variance(grades)

for grade in grades:
  print grade
print grades_sum(grades)
print grades_average(grades)
print grades_variance(grades)
print grades_std_deviation(variance)



# list slicing Syntext

    l = [i ** 2 for i in range(1, 11)]
    # Should be [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

    print l[2:9:2]


    # omitting indices
    my_list = range(1, 11) # List of numbers 1 - 10

    # Add your code below!
    print my_list[::2]


    # Reverse list
    my_list = range(1, 11)

    # Add your code below!
    backwards = my_list[::-1]


# Stride length

to_one_hundred = range(101)
# Add your code below!

backwards_by_tens = to_one_hundred[::-10]
print backwards_by_tens



# Practice Makes Perfect

to_21 = range(1, 22)

odds = to_21[::2]

middle_third = to_21[7:14]


# Anonymous Functions
my_list = range(16)
print filter(lambda x: x % 3 == 0, my_list)




# Lambda Syntax
languages = ["HTML", "JavaScript", "Python", "Ruby"]

# Add arguments to the filter()
print filter(lambda x: x == "Python", languages)



# Try it
squares = [x ** 2 for x in range(1, 11)]

print filter(lambda x: x >= 30 and x <= 70, squares)



# Iterating Over Dictionaries
movies = {
  "Monty Python and the Holy Grail": "Great",
  "Monty Python's Life of Brian": "Good",
  "Monty Python's Meaning of Life": "Okay"
}

print movies.items()


# Comprehending Comprehensions
threes_and_fives = [x for x in range(1, 16) if x % 3 == 0 or x % 5 == 0]




# list slicing

garbled = "!XeXgXaXsXsXeXmX XtXeXrXcXeXsX XeXhXtX XmXaX XI"
message = garbled[::-2]


# Lambda Expression

garbled = "IXXX aXXmX aXXXnXoXXXXXtXhXeXXXXrX sXXXXeXcXXXrXeXt mXXeXsXXXsXaXXXXXXgXeX!XX"

message = filter(lambda x: x != "X", garbled)
print message


# Just a Little BIT
print 5 >> 4  # Right Shift
print 5 << 1  # Left Shift
print 8 & 5   # Bitwise AND
print 9 | 4   # Bitwise OR
print 12 ^ 42 # Bitwise XOR
print ~88     # Bitwise NOT



# Lesson I0: The Base 2 Number System
print 0b1,    #1
print 0b10,   #2
print 0b11,   #3
print 0b100,  #4
print 0b101,  #5
print 0b110,  #6
print 0b111   #7
print "******"
print 0b1 + 0b11
print 0b11 * 0b11




# count 1 to 12
one = 0b1
two = 0b10
three = 0b11
four =0b100
five = 0b101 
six = 0b110
seven =0b111
eight = 0b1000
nine = 0b1001
ten = 0b1010
eleven = 0b1011
twelve = 0b1100


# The bin() Function

print bin(1)
print bin(2)
print bin(3)
print bin(4)
print bin(5)
print bin(6)


# int second parameter

print int("1",2)
print int("10",2)
print int("111",2)
print int("0b100",2)
print int(bin(5),2)
# Print out the decimal equivalent of the binary 11001001.
print int("11001001", 2)



# Slide to the left
shift_right = 0b1100
shift_left = 0b1

# Your code here!
shift_right = shift_right >> 2
shift_left = shift_left << 2

print bin(shift_right)
print bin(shift_left)


# A BIT of This AND That (print bin(0b1110 & 0b101))
# A BIT of This OR That (print bin(0b1110 | 0b101))
# This XOR That?(print bin(0b1110 ^ 0b101))

# See? This is NOT That Hard!
print ~1
print ~2
print ~3
print ~42
print ~123

# The Man Behind the Bit Mask
def check_bit4(input):
  mask = 0b1000
  desired = input & mask
  if desired > 0:
    return "on"
  else:
    return "off"


# Turn It On
a = 0b10111011

mask = 0b100
desired = a | mask
print bin(desired)



# just fit out
a = 0b11101110
mask = 0b11111111
desired = a ^ mask
print bin(desired)



# slip and slide
def flip_bit(number, n):
  bit_to_flip = 0b1 << (n -1)
  result = number ^ bit_to_flip
  return bin(result)


# RGB hex converter project

def rgb_hex():
  invalid_msg = "Invalid value entered"
  red = int(input("Enter a red value: "))
  if red < 0 or red > 255:
    print(invalid_msg)
    return
  green = int(input("Enter a green value: "))
  if green < 0 or green > 255:
    print(invalid_msg)
    return
  blue = int(input("Enter a blue value: "))
  if blue < 0 or blue > 255:
    print(invalid_msg)
    return
  val = (red << 16) + (green << 8) + blue
  print(str(hex(val[2::]))).upper()
def hex_rgb():
  hex_val = input("Enter the hexadecimal value: ")
  if len(hex_val) != 6:
    print("Invalid hexadecimal value")
    return
  else:
    hex_val = int(hex_val, 16)
  two_hex_digits = 2 ** 8
  blue = hex_val % two_hex_digits
  hex_val = hex_val >> 8
  green = hex_val % two_hex_digits
  hex_val = hex_val >> 8
  red = hex_val % two_hex_digits
  print("Red:" , red , "Green:" , green , "Blue:" , blue)
def convert():
    while True:
      option = input("Enter 1 to convert RGB to HEX. Enter 2 to convert HEX to RGB. Enter X to Exit: ")
      if option == '1':
        print "RGB to Hex..."
        rgb_hex()
      elif option == '2':
        print("Hex to RGB...")
        hex_rgb()
      elif option == 'X' or option == 'x':
        break
      else:
        print("Error")
convert()






# Why used classes
class Fruit(object):
  """A class that makes various tasty fruits."""
  def __init__(self, name, color, flavor, poisonous):
    self.name = name
    self.color = color
    self.flavor = flavor
    self.poisonous = poisonous

  def description(self):
    print "I'm a %s %s and I taste %s." % (self.color, self.name, self.flavor)

  def is_edible(self):
    if not self.poisonous:
      print "Yep! I'm edible."
    else:
      print "Don't eat me! I am super poisonous."

lemon = Fruit("lemon", "yellow", "sour", False)

lemon.description()
lemon.is_edible()



# Class Syntax
class Animal(object):
  pass


# Classier Classes
class Animal(object):
  def __init__(self):
    pass


# Let not gote too selfies
class Animal(object):
  def __init__(self, name):
    self.name = name
    
    
# Instantiating Your First Object
class Animal(object):
  def __init__(self, name):
    self.name = name
    
zebra = Animal("Jeffrey")
print zebra.name


# more in inite
# Class definition
class Animal(object):
  """Makes cute animals."""
  # For initializing our instance objects
  def __init__(self, name, age, is_hungry):
    self.name = name
    self.age = age
    self.is_hungry = is_hungry

# Note that self is only used in the __init__()
# function definition; we don't need to pass it
# to our instance objects.

zebra = Animal("Jeffrey", 2, True)
giraffe = Animal("Bruce", 1, False)
panda = Animal("Chad", 7, True)

print zebra.name, zebra.age, zebra.is_hungry
print giraffe.name, giraffe.age, giraffe.is_hungry
print panda.name, panda.age, panda.is_hungry



# https://www.codecademy.com/courses/learn-python/lessons/introduction-to-classes/exercises/more-on-init-and-self