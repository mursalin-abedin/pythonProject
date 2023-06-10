# 08 For Loops

# They are used to repeat a task
# In this example we are trying to send a message to a use at least 3 time
#In Python, the for loop is used to run a block of code for a certain number of times.
# It is used to iterate over any sequences such as list, tuple, string, etc.

for number in range(3):  # the range goes from 0, 1, 2
    print("Attempt", number + 1, (number + 1) * ".")

for number in range(1, 4):  # range goes from 1, 2, 3
    print("Attempt", number, number * ".")

for number in range(1, 10, 2):  # range goes from 1, 3, 5, 7, 9
    print("Attempt", number, number * ".")

for tasmi in range(10):  # inst of number I have used range
    print("Tasmi is good boy", tasmi + 1, tasmi - 1)

for laptop in range(8):  # the range goes form Zero to Eight, starts with syntax "for" syntax "in"
    print("laptop")

languages = ['Swift', 'Python', 'Go', 'JavaScript']

# access items of a list using for loop
for language in languages:
    print(language)

