# 08 Working with Numbers
# to Import the math module type command - import math - , to be able to use more math functions
import math
print(round(2.9595, 2))  # Function to round numbers
print(abs(-5.4))  # Converts a number to absolute
print(math.ceil(8.2))  # Math function to return the ceil of a float number
print(math.floor(4.9))

average = 2.9
print(f"{average:.2f}")


#Use the format() method to insert numbers into strings:
age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))
