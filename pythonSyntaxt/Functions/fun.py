# What Good are Functions?

def tax(bill):
  """Adds 8% tax to a restaurant bill."""
  bill *= 1.08
  print "With tax: %f" % bill
  return bill

def tip(bill):
  """Adds 15% tip to a restaurant bill."""
  bill *= 1.15
  print "With tip: %f" % bill
  return bill
  
meal_cost = 100
meal_with_tax = tax(meal_cost)
meal_with_tip = tip(meal_with_tax)

# Functions Junction

ef spam():
  """Prints 'Eggs!'"""
  print "Eggs!"

# Define the spam function above this line.
spam()

# Call and Response

def square(n):
  """Returns the square of a number."""
  squared = n ** 2
  print "%d squared is %d." % (n, squared)
  return squared
  
# Call the square function on line 10! Make sure to
# include the number 10 between the parentheses.

square(10)

# Parameter and Argument
def power(base, exponent):  # Add your parameters here!
  result = base ** exponent
  print "%d to the power of %d is %d." % (base, exponent, result)

power(37, 4)  # Add your arguments here!


# Function Calling Function

def one_good_turn(n):
  return n + 1
    
def deserves_another(n):
  return one_good_turn(n) + 2

# Practice Makes Perfect

def cube(number):
  return number * number * number

def by_three(number):
  if number % 3 == 0:
    return cube(number)
  else:
    return False


# new
# Ask Python to print sqrt(25) on line 3.
import math
print math.sqrt(25)



# Function import

from math import sqrt

# Universal import

from module import *

#  Here Be dragon

from module import * # Imports the math module
everything = dir(math) # Sets everything to a list of things from math
print everything # Prints 'em all!

# one beyond String
def biggest_number(*args):
  print max(args)
  return max(args)
    
def smallest_number(*args):
  print min(args)
  return min(args)

def distance_from_zero(arg):
  print abs(arg)
  return abs(arg)

biggest_number(-10, -5, 5, 10)
smallest_number(-10, -5, 5, 10)
distance_from_zero(-10)


# Max
# Set maximum to the max value of any set of numbers on line 3!

maximum = max(4, 8, 15)

print maximum

# Minimum

# Set minimum to the min value of any set of numbers on line 3!

minimum = min(4, 8, 15)

print minimum


# abs
absolute = abs(-42)

print absolute

# Type

# Print out the types of an integer, a float,
# and a string on separate lines below.
print type('I have to push the pram a lot')
print type(4)
print type(4.9)



# Reviews:Function

def shut_down(s):
  if s == "yes":
    return "Shutting down"
  elif s == "no":
    return "Shutdown aborted"
  else:
    return "Sorry"


# Review Module

import math
print math.sqrt(13689)

# Review: Built-In Functions

def distance_from_zero(num):
  if type(num) == int or type(num) == float:
    return abs(num)
  else:
    return "Nope"

# 