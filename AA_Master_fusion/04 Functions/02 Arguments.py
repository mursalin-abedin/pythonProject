# 02 Arguments


def greet(first_name, last_name):
    print(f"Hi there {first_name} {last_name}")
    print("Welcome aboard")


greet("Miguel", "Pimenta")
greet("M", "Abedin")


# Normal Arguments
def my_function(fname, lname):
    print(fname + " " + lname)


my_function("Emil", "Stevens")


# Arbitrary Arguments Is Infinite, Not Specified
def my_function(*kids):
    print("The youngest child is " + kids[2])


my_function("Emil", "Tobias", "Linus")


# Keyword Arguments
def my_function(child3, child2, child1):
    print("The youngest child is " + child3)


my_function(child1="Emil", child2="Tobias", child3="Linus")


# If Keyword Arguments is Infinite, Not Specified
def my_function(**kid):
    print("His last name is " + kid["yname"])


my_function(fname="Tobias", lname="Refsnes", sname="fefe", yname="llwglen")
