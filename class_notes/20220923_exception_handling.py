"""
Exceptions and exception handling
try/except blocks

You can have multiple except blocks
- each can handle a specific exception
- alternatively, you can use a general except and use 'pass' keyword
  - doesn't care, just skip over it
  - general except is a catch-all
  - rule of thumb, try to handle specific errors
  - no general except, the interpreter blows up and ends to program

RAISING EXCEPTIONS
- introduce error checking code if a wrong type is input, example
  - "two hundred" entered for a weight, example
  - a height less than or equal to 0, example

Can handle w/ if, else statements w/ prints
or actually utilize raise

if weight < 0:
    raise ValueError('Invalid weight').

except ValueError as excpt:
    print(excpt)
    print('Could not calculate health info.\n')

creates a new exception of that type

custome errors can be created

EXCEPTIONS WITH FUNCTIONS
exceptions can be handled w/in the function
or, an exception handler can be put in place at the point of call

USING FINALLY TO CLEAN UP
finally keyword executes that block of code regardless of any exceptions
- closing a file is a good example of this
- always the last block of code before the try finishes
===
If no exception occurs, then execution continues in the finally clause,
and then proceeds w/ the rest of the program.
If a handled exception occurs, then an exception handler executes and
then the finally clause.
If an unhandled exception occurs, then the finally clause executes and
then the exception is re-raised.
The finally clause also executes if any break, continue, or return
statment causes the try block to be exited.
===

you can have as many exception handlers as desired but a finally clause
must be at the end

CUSTOM EXCEPTION TYPES
class LessThanZeroError(Exception)
-->extends the exception class
    def __init__(self, value):
        self.value = value)

my_num = int(input('Enter a number: ')

if my_num < 0:
    raise LessThanZeroError('my_num must be greater than 0')
else:
    print('my_num:', my_num)

the __init__ allows us to define our own parameters for the exception
- overrides the contructor of the Exception class
the __str__ allows us to modify the text of the error

More info:
https://www.programiz.com/python-programming/user-defined-exception


"""