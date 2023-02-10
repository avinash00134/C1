numbers = [5, 6, 7, 8]

print "Adding the numbers at indices 0 and 2..."
print numbers[0] + numbers[2]
print "Adding the numbers at indices 1 and 3..."
# Your code here!
print numbers[1] + numbers[3]

# new Nebour
zoo_animals = ["pangolin", "cassowary", "sloth", "tiger"]
# Last night our zoo's sloth brutally attacked 
# the poor tiger and ate it whole.

# The ferocious sloth has been replaced by a friendly hyena.
zoo_animals[2] = "hyena"

# What shall fill the void left by our dear departed tiger?
# Your code here!
zoo_animals[3] = "lion"

# Arivvel and list

suitcase = [] 
suitcase.append("sunglasses")

# Your code here!
suitcase.append("shirt")
suitcase.append("pants")
suitcase.append("shoes")

list_length = len(suitcase) # Set this to the length of suitcase

print "There are %d items in the suitcase." % (list_length)
print suitcase

#  List Scalling

suitcase = ["sunglasses", "hat", "passport", "laptop", "suit", "shoes"]

# The first and second items (index zero and one)
first = suitcase[0:2]

# Third and fourth items (index two and three)
middle = suitcase[2:4]

# The last two items (index four and five)
last = suitcase[4:6]

# Slicing list and String

animals = "catdogfrog"

# The first three characters of animals
cat = animals[:3]

# The fourth through sixth characters
dog = animals[3:6]

# From the seventh character to the end
frog = animals[6:]



# Maintaing order
animals = ["aardvark", "badger", "duck", "emu", "fennec fox"]
duck_index = animals.index("duck")# Use index() to find "duck"

# Your code here!
animals.insert(duck_index,"cobra")

print animals # Observe what prints after the insert operation


# for one and all\
    
my_list = [1,9,3,8,5,7]

for number in my_list:
  # Your code here
  print 2 * number
  
  
  
# more with for

start_list = [5, 3, 1, 2, 4]
square_list = []

# Your code here!
for num in start_list:
  square_list.append(num ** 2)
square_list.sort()

print square_list

# This Next Part is Key

# Assigning a dictionary with three key-value pairs to residents:
residents = {'Puffin' : 104, 'Sloth' : 105, 'Burmese Python' : 106}

print residents['Puffin'] # Prints Puffin's room number

# Your code here!
print residents['Sloth']
print residents['Burmese Python']


# New Entries

menu = {} # Empty dictionary
menu['Chicken Alfredo'] = 14.50 # Adding new key-value pair
print menu['Chicken Alfredo']

# Your code here: Add some dish-price pairs to menu!
menu['valu'] = 115.50
menu['Pizza '] = 8.50
menu['choclate'] = 20.00

print "There are " + str(len(menu)) + " items on the menu."
print menu

# Changing your mind

# key - animal_name : value - location 
zoo_animals = { 'Unicorn' : 'Cotton Candy House',
'Sloth' : 'Rainforest Exhibit',
'Bengal Tiger' : 'Jungle House',
'Atlantic Puffin' : 'Arctic Exhibit',
'Rockhopper Penguin' : 'Arctic Exhibit'}
# A dictionary (or list) declaration may break across multiple lines

# Removing the 'Unicorn' entry. (Unicorns are incredibly expensive.)
del zoo_animals['Unicorn']

# Your code here!
del zoo_animals['Sloth']
del zoo_animals['Bengal Tiger']
zoo_animals['Rockhopper Penguin'] = 'Plains Exhibit'

print zoo_animals

# Remove a Few Things

backpack = ['xylophone', 'dagger', 'tent', 'bread loaf']
backpack.remove('dagger')


# BeFOR We Begin

 names = ["Adam","Alex","Mariah","Martine","Columbus"]

for name in names:
  print name
  
#  This is key

webster = {
  "Aardvark" : "A star of a popular children's cartoon show.",
  "Baa" : "The sound a goat makes.",
  "Carpet": "Goes on the floor.",
  "Dab": "A small amount."
}

# Add your code below!
for w in webster:
  print webster[w]


# Control and flow looping
a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

for number in a:
  if number % 2 == 0:
    print number


# list + Functions
# Write your function below!
def fizz_count(x):
  count = 0
  for item in x:
    if item == "fizz":
      count = count + 1
  return count
  
  
#   String Looping

for letter in "Codecademy":
  print letter
    
# Empty lines to make the output pretty
print
print

word = "Programming is fun!"

for letter in word:
  # Only print out the letter i
  if letter == "i":
    print letter
    
# Your own Store

pricesd = {
  "banana" :4,
   "apple": 2, 
   "orange":1.5,
   "pear":3 }
# investing in the stock

pricesd = {
  "banana" :4,
   "apple": 2, 
   "orange":1.5,
   "pear":3 }
stock = {
  "banana": 6,
   "apple": 0, 
   "orange": 32, 
   "pear": 15
}

# Keeping Track of the Produce
prices = {"banana": 4,"apple": 2,"orange": 1.5,"pear": 3}

stock = {"banana": 6, "apple": 0, "orange": 32, "pear": 15}

for food in prices:
  print food
  print "price: %s" % prices[food]
  print "stock: %s" % stock[food]
  
#   Something of Value

prices = {"banana": 4,"apple": 2,"orange": 1.5,"pear": 3}

stock = {"banana": 6, "apple": 0, "orange": 32, "pear": 15}

total = 0
for food in prices:
  print prices[food] * stock[food]
  total = total + prices[food] * stock[food]
print total

# Shopping at the Market

# Making a Purchase
shopping_list = ["banana", "orange", "apple"]

stock = {
  "banana": 6,
  "apple": 0,
  "orange": 32,
  "pear": 15
}
    
prices = {
  "banana": 4,
  "apple": 2,
  "orange": 1.5,
  "pear": 3
}

# Write your code below!
def compute_bill(food):
  total = 0
  for item in food:
    total = total + prices[item]
  return total


# Stocking out
shopping_list = ["banana", "orange", "apple"]

stock = {
  "banana": 6,
  "apple": 0,
  "orange": 32,
  "pear": 15
}
    
prices = {
  "banana": 4,
  "apple": 2,
  "orange": 1.5,
  "pear": 3
}

# Write your code below!
def compute_bill(food):
  total = 0
  for item in food:
    if stock[item] > 0:
      total += prices[item]
      stock[item] -= 1
  return total


# project Rock, Peaper and sci

'''
Codeacedemy
Rock, Paper, Scissor'''

from random import randint

options = ["ROCK", "PAPER", "SCISSORS"]

message = {
  "tie" : "Yawn it's a tie!",
  "won" : "Yay you won!",
  "lost": "Aww you lost!"
}

def decide_winner(user_choice, computer_choice):
  user_choice = "You selected: %s" % user_choice
  print user_choice
  computer_choice = "Computer selected: %s" %computer_choice
  print computer_choice

  if user_choice == computer_choice:
    print message['tie']
  elif user_choice == options[0] and computer_choice == options[2]:
    print message["won"]
  elif user_choice == options[1] and computer_choice == options[0]:
    print message["won"]
  elif user_choice == options[2] and computer_choice == options[1]:
    print message["won"]
  else:
    print message["lost"]
  
def play_RPS():
  user_choice = raw_input("Enter Rock, Paper, Scissors: ")
  user_choice = user_choice.upper()
  computer_choice = options[randint(0, 2)]
  decide_winner(user_choice, computer_choice)

play_RPS()

# How is Everybody Doing?

lloyd = {
  "name": "Lloyd",
  "homework": [90.0, 97.0, 75.0, 92.0],
  "quizzes": [88.0, 40.0, 94.0],
  "tests": [75.0, 90.0]
}
student = ["alice","lloyd","tyler"]
alice = {
  "name": "Alice",
  "homework": [100.0, 92.0, 98.0, 100.0],
  "quizzes": [82.0, 83.0, 91.0],
  "tests": [89.0, 97.0]
}
tyler = {
  "name": "Tyler",
  "homework": [0.0, 87.0, 75.0, 22.0],
  "quizzes": [0.0, 75.0, 78.0],
  "tests": [100.0, 100.0]
}

def average(numbers):
  total = sum(numbers)
  total = float(total)
  return total/len(numbers)

def get_average(student):
  homework = average(student["homework"])
  quizzes = average(student["quizzes"])
  tests = average(student["tests"])
  return 0.1 * homework + 0.3 * quizzes + 0.6 * tests

def get_letter_grade(score):
  if score >= 90:
    return "A"
  elif score >=80:
    return "B"
  elif score >=70:
    return "C"
  elif score >=60:
    return "D"
  else:
    return "F"

def get_class_average(class_list):
  results = []
  for student in class_list:
    student_avg = get_average(student)
    results.append(student_avg)
  return average(results)



    


