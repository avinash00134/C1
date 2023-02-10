my_dict = {
  'name': 'Nick',
  'age':  31,
  'occupation': 'Dentist',
}

print my_dict.items()

# keys() and values()
`my_dict = {
  'name': 'Nick',
  'age':  31,
  'occupation': 'Dentist',
}

print my_dict.keys()
print my_dict.values()


# The 'in' Operator


my_dict = {
  'name': 'Nick',
  'age':  31,
  'occupation': 'Dentist',
}

for key in my_dict:
  print key, my_dict[key]
  
#Building Lists
evens_to_50 = [i for i in range(51) if i % 2 == 0]
print evens_to_50

# List Comprehension Syntax

doubles_by_3 = [x * 2 for x in range(1, 6) if (x * 2) % 3 == 0]

# Complete the following line. Use the line above for help.
even_squares = [x ** 2 for x in range(1, 12) if x % 2 == 0]

print even_squares


# now you Try
cubes_by_four = [x ** 3 for x in range(1, 11) if ((x ** 3) % 4) == 0]
print cubes_by_four