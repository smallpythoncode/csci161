"""
Some new stuff...hopefully

Keyword arguments - allows the passing of arguments by name rather
than by position
- General guideline: use keyword arguments for any func containing
more than 4 arguments
- can be mixed with positional arguments given keyword arguments are
given last

Default parameter values - essentially creates optional arguments
- will call the default value if not specified
- will be overwritten if argument is specified

- DON'T PUT A MUTABLE OBJECT AS A DEFAULT PARAMETER. It will change
the instance of the list. If you need to modify yet keep the original
mutable object, create a copy and return it if necessary

def some_func(my_list=None):
    if my_list == None:
    # if my_list is None:
        # creates a blank copy of my_list
        my list = []

You can mix keyword arguments and default parameter values

ARBITRARY ARGUMENT LISTS
Sometimes a programmer doesn't know how many arguments a function
requires
- A func can include the *args parameter that collections
optional positional arguments into an arbitrary arguments list

**kwargs creates a dictionary
- key and associated value

MULTIPLE FUNCTION OUTPUTS
"return r1, r2" will return a tuple
- not limited to a tuple, can be any container

DOCSTRINGS
can serve as a comment w/in the code
can use help() to print the docstrings

Segregate your code
- don't put computational code in places where it is only calculated
once if it only needs to be calculated once
  - depending on the function, calculations may be very taxing
  - don't redo math that's already been done or only needs to be
  calculated once
"""