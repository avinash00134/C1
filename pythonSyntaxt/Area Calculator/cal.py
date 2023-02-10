'''Codeacedemy
Area calaculator'''

print "The calculator is starting up."

option = raw_input("Enter C for Circle or T for Triangle: ")
option = option.upper()

if option == "C":
  radius = float(raw_input("Enter the radius: "))
  area = 3.14159 * radius ** 2
  print "Area of circle is: %d" % (area)
elif option == "T":
  base = float(raw_input("Enter the base: "))
  height = float(raw_input("Enter the height: "))
  area = 0.5 * base * height
  print "Area of triangle is: %s" % (area)
