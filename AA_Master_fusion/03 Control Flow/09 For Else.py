# 09 For..Else

# Lesson how to break a for loop

successful = False
for number in range(3):
    print("Attempt")
    if successful:
        print("Successful")
        break
else:
    print("Attempted 3 times and failed")

# Another Example
digits = [0, 1, 5]

for i in digits:
    print(i)
else:
    print("No items left.")


# Under this line Practice
models = ['Civic', 'RDX', 'MDX', 'TLX']

for i in models:
    print(i)
else:
    print("Here is all the Honda Model.")

games = ['Call of duty', 'Fifa', 'Candy Crush']

for b in games:
    print(b)
