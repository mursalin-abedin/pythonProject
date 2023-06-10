# 07 Numbers
# Type of numbers in Python
x = 3  # Integer number (পূর্ণসংখ্যা)
y = 3.1  # Float number (ভগ্নাংশ)
z = 3 + 2j  # Complex number a + bi

print(10 + 3)  # Addition
print(10 - 3)  # Subtraction
print(10 * 3)  # Multiplication
print(10 / 3)  # Division
print(10 // 3)  # Division but returns an integer
print(10 % 3)  # Remainder of division
print(10 ** 3)  # Exponent

x = x + 3
print(x)
y += 3
print(y)

# To verify the type of any object in Python, use the type() function:
print(type(x))

# It tells us x =3 is an Integer Number
print(type(y))

# It tells us x =3 is a Float Number
print(type(z))

# Convert from one type to another:
x = 1  # int
y = 2.8  # float
z = 1j  # complex

# convert from int to float:
a = float(x)

# convert from float to int:
b = int(y)

# convert from int to complex:
c = complex(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))

# You can assign a multiline string to a variable by using three quotes:
a = """A Python library is a collection of related modules. 
It contains bundles of code that can be used repeatedly in different programs. 
It makes Python Programming simpler and convenient for the programmer. 
As we don’t need to write the same code again and again for different programs.
Python libraries play a very vital role in fields of Machine Learning, Data Science, 
Data Visualization, etc."""
print(a)

b = """পাইথন একটি হাই-লেভেল স্ক্রিপটিং প্রোগ্রামিং ল্যাংগুয়েজ, যা লিখেছেন Guido Van Rossum।"""
print(b)
