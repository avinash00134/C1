ministry = "The Ministry of Silly Walks"

print len(ministry)
print ministry.upper()


# printing Variables

the_machine_goes = "Ping!"
print the_machine_goes

# String concatanations

print "Spam " + "and " + "eggs"

# Explicit String

print "The value of pi is around " + str(3.14)

# String Formatting

string_1 = "Camelot"
string_2 = "place"

print "Let's not go to %s. 'Tis a silly %s." % (string_1, string_2)

# String formatting 2

name = "Alex"
quest = "Teaching Python"
color = "Blue"

print "Ah, so your name is %s, your quest is %s, " \
"and your favorite color is %s." % (name, quest, color)

# And Now, For Something Completely Familiar

# Write your code below, starting on line 3!
my_string = "Any your like"
print(len(my_string))
print  my_string.upper()


# DATE A TIME d
# datetime library
from datetime import datetime

# current date
ffrom datetime import datetime
now = datetime.now()
print now



# Exracting info
from datetime import datetime
now = datetime.now()
print now
print now.year
print now.month
print now.day

# Hot date
from datetime import datetime
now = datetime.now()
print '%02d/%02d/%04d' % (now.month, now.day, now.year)

from datetime import datetime
now = datetime.now()

print '%02d:%02d:%02d' % (now.hour, now.minute, now.second)


print '%02d/%02d/%04d %02d:%02d:%02d' % (now.month, now.day, now.year, now.hour, now.minute, now.second)


# CONDITIONALS & CONTROL FLOW 
# Go With the Flow

def clinic():
    print "You've just entered the clinic!"
    print "Do you take the door on the left or the right?"
    answer = raw_input("Type left or right and hit 'Enter'.").lower()
    if answer == "left" or answer == "l":
        print "This is the Verbal Abuse Room, you heap of parrot droppings!"
    elif answer == "right" or answer == "r":
        print "Of course this is the Argument Room, I've told you that already!"
    else:
        print "You didn't pick left or right! Try again."
        clinic()

clinic()

# CONDITIONALS & CONTROL FLOW
# Compare Closely!

# Assign True or False as appropriate on the lines below!

# Set this to True if 17 < 328 or to False if it is not.
bool_one = True   # We did this one for you!

# Set this to True if 100 == (2 * 50) or to False otherwise.
bool_two = True

# Set this to True if 19 <= 19 or to False if it is not.
bool_three = False

# Set this to True if -22 >= -18 or to False if it is not.
bool_four = False

# Set this to True if 99 != (98 + 1) or to False otherwise.
bool_five = False

# CONDITIONALS & CONTROL FLOW
# Compare... Closelier!

# Assign True or False as appropriate on the lines below!

# (20 - 10) > 15
bool_one = False    # We did this one for you!

# (10 + 17) == 3**16
# Remember that ** can be read as 'to the power of'. 3**16 is about 43 million.
bool_two = False

# 1**2 <= -1
bool_three = False

# 40 * 4 >= -4
bool_four = True

# 100 != 10**2
bool_five = False

# CONDITIONALS & CONTROL FLOW 
# How the Tables Have Turned

# Create comparative statements as appropriate on the lines below!

# Make me true!
bool_one = 3 < 5  # We already did this one for you!

# Make me false!
bool_two = False

# Make me true!
bool_three = True

# Make me false!
bool_four = True

# Make me true!
bool_five = True

# CONDITIONALS & CONTROL FLOW
# And
bool_one = False and False

bool_two = -(-(-(-2))) == -2 and 4 >= 16 ** 0.5

bool_three = 19 % 4 != 300 / 10 / 10 and False

bool_four = -(1 ** 2) < 2 ** 0 and 10 % 10 <= 20 - 10 * 2

bool_five = True and True

# Or

bool_one = 2 ** 3 == 108 % 100 or 'Cleese' == 'King Arthur'

bool_two = True or False

bool_three = 100 ** 0.5 >= 50 or False

bool_four = True or True

bool_five = 1 ** 100 == 100 ** 1 or 3 * 2 * 1 != 3 + 2 + 1

# Not

bool_one = not True

bool_two = not 3**4<4**3

bool_three = not 10%3 <= 10 %2

bool_four = not 3**2 +4**2 !=5**2

bool_five = not not False

# This and That (or This, But Not That!)

bool_one = False or not True and True

bool_two = False and not True or True

bool_three = True and not(False or False)

bool_four = not not True or False and not True

bool_five = False or not (True and True )

# Conditional Statement Syntax

response = 'Y'

answer = "Left"
if answer == "Left":
    print "This is the Verbal Abuse Room, you heap of parrot droppings!"


# If you are having

def using_control_once():
    if True:
        return "Success #1"

def using_control_again():
    if True:
        return "Success #2"

print using_control_once()
print using_control_again()

# Else Problems, I Feel Bad for You, Son...

answer = "'Tis but a scratch!"

def black_knight():
    if answer == "'Tis but a scratch!":
        return True
    else:             
        return False        # Make sure this returns False

def french_soldier():
    if answer == "Go away, or I shall taunt you a second time!":
        return True
    else:             
        return False        # Make sure this returns False
    
# I Got 99 Problems, But a Switch Ain't One
def greater_less_equal_5(answer):
    if answer > 5:
        return 1
    elif answer < 5:          
        return -1
    else:
        return 0
        
print greater_less_equal_5(4)
print greater_less_equal_5(5)
print greater_less_equal_5(6)


# The Big If

# Complete the if and elif statements!
def grade_converter(grade):
    if grade >= 90:
        return "A"
    elif grade >= 80:
        return "B"
    elif grade >= 70:
        return "C"
    elif grade >= 65:
        return "D"
    else:
        return "F"
      
# This should print an "A"      
print grade_converter(92)

# This should print a "C"
print grade_converter(70)

# This should print an "F"
print grade_converter(61)


    