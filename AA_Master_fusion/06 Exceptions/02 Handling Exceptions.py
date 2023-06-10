# 02 Handling Exceptions

# To handle exceptions we have to put the statement in a try block When Python sees a try block it will execute every
# statement in this block, if any of the statements throws an exception, the code in the exception block will be
# executed. If no exception are thrown the code in the execution block will not be executed.

try:  # try block
    age = int(input("Age: "))
except ValueError as ex:  # In this cde we are handling ValueError exception for non-numeric values. "as ex" we can
    # add a variable that will include details about the execution.
    print("You did no enter a valid age.")
    print(ex)
    print(type(ex))
else:  # An optional else block can be added. The code we add here will be executed if no executions occur
    print('No exceptions where thrown')

print("Executions continues")  # Because we are handling this exception properly the line will be executed, and the
# program will not crash
try:
    code =int(input("Type your Project code"))
except ValueError as ex:

    print("Honda Project Code only")

