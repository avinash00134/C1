# 1
def answer():
  return 42

# Planning Your Trip

def hotel_cost(nights):
  return 140 * nights

# Getting There

def hotel_cost(nights):
  return 140 * nights

def plane_ride_cost(city):
  if city == "Charlotte":
    return 183
  elif city == "Tampa":
    return 220
  elif city == "Pittsburgh":
    return 222
  elif city == "Los Angeles":
    return 475

# Transportation

def hotel_cost(nights):
  return 140 * nights

def plane_ride_cost(city):
  if city == "Charlotte":
    return 183
  elif city == "Tampa":
    return 220
  elif city == "Pittsburgh":
    return 222
  elif city == "Los Angeles":
    return 475

def rental_car_cost(days):
  cost = days * 40
  if days >= 7:
    cost -= 50
  elif days >= 3:
    cost -= 20
  return cost

# Pull it Together
def hotel_cost(nights):
  return 140 * nights

def plane_ride_cost(city):
  if city == "Charlotte":
    return 183
  elif city == "Tampa":
    return 220
  elif city == "Pittsburgh":
    return 222
  elif city == "Los Angeles":
    return 475

def rental_car_cost(days):
  cost = days * 40
  if days >= 7:
    cost -= 50
  elif days >= 3:
    cost -= 20
  return cost

def trip_cost(city, days):
  return rental_car_cost(days) + hotel_cost(days - 1) + plane_ride_cost(city)

# Hey, You Never Know!
def hotel_cost(nights):
  return 140 * nights

def plane_ride_cost(city):
  if city == "Charlotte":
    return 183
  elif city == "Tampa":
    return 220
  elif city == "Pittsburgh":
    return 222
  elif city == "Los Angeles":
    return 475

def rental_car_cost(days):
  cost = days * 40
  if days >= 7:
    cost -= 50
  elif days >= 3:
    cost -= 20
  return cost

def trip_cost(city, days,spending_money):
  return rental_car_cost(days) + hotel_cost(days - 1) + plane_ride_cost(city)+spending_money

# Plane your trip

def hotel_cost(nights):
  return 140 * nights

def plane_ride_cost(city):
  if city == "Charlotte":
    return 183
  elif city == "Tampa":
    return 220
  elif city == "Pittsburgh":
    return 222
  elif city == "Los Angeles":
    return 475

def rental_car_cost(days):
  cost = days * 40
  if days >= 7:
    cost -= 50
  elif days >= 3:
    cost -= 20
  return cost

def trip_cost(city, days, spending_money):
  return rental_car_cost(days) + hotel_cost(days) + plane_ride_cost(city) + spending_money

print trip_cost("Los Angeles", 5, 600)

# Number Guess project

'''
Codeacedemy
Number guess'''

from random import randint
from time import sleep

def get_user_guess():
  guess = int(raw_input("Guess a number: "))
  return guess

def roll_dice(number_of_sides):
  first_roll = randint (1, 6)
  second_roll = randint (1, 6)
  max_val = number_of_sides * 2
  print ("Maximun possible value is %d" %(max_val))
  guess = get_user_guess()
  if guess > max_val:
    print "No guessing higher than the maximum possible value!"
  else:
    print "Rolling..."
    sleep(1)
    print (second_roll)
    sleep(1)
    total_roll = first_roll + second_roll
    print "Result..."
    sleep(1)
    if guess == total_roll:
      print "You won!"
    else:
      print "You lost!"
      

roll_dice(6)

