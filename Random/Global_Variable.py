x = "awesome"


def myfunc():
    x = "fantastic"
    print("Python is " + x)


myfunc()

print("Python is " + x)

# Global Keyword
# Can be access from anywhere.It is  not recommended

# Practice
y = "apple"


def mycode():
    y = "Healthy"
    print(y + " is a healthy food")


# y= apple is not going to act here anymore. We have stored a new value to healthy.
mycode()
print("I love " + y)
print('Hey.', 'Are you enjoying the course?')
print('Hey')
print('How are you?')

# global_var is in the global namespace
global_var = 10
#Another Example
def outer_function():
    #  outer_var is in the local namespace
    outer_var = 20

    def inner_function():
        #  inner_var is in the nested local namespace
        inner_var = 30

        print(inner_var)

    print(outer_var)

    inner_function()

# print the value of the global variable
print(global_var)

# call the outer function and print local and nested local variables
outer_function()