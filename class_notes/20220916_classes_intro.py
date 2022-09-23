"""
nordlie.cs.und.edu/weather/weather_info.html
- radar loop and current weather conditions at GFK

nordlie.cs.und.edu/weather/make_new_file.py

.json() is integrated into requests

bash shell to run the radar loop
nordlie.cs.und.edu/weather/doit

what is cron tab?
what is a .tif?
- tagged image format?
what is a .gif?

./gifsicle - used for animating gif loops

the bash shell fires of the .py file

doing some of this kind of stuff (pulling data from
the web) may require an API key
!! SAFEGUARD API KEYS !!
Do NOT put them in public view
"""

"""
mapping keys
can be used as a method of formatting strings
02d: - zero pad on the left
--> '02' rather than '2'
"""

"""
Chapter 9 - Classes

Abstraction occurs when a user interacts w/ an object at a high level,
allowing lower-lever internal details to remain hidden
- "the black box"
- Do we really need to know how things work on the back end?

Abstract data type (ADT) is a data type whose creation and update
are constrained to specific well-defined operations
- classes are an implementation of this

UML - unified markup language

CLASSES are about grouping data, including functions
class keyword can be used to create a user-defined type of object containing
groups of related variables and functions

the object maintains a set of attributes that determines the data and
behavior of the class

class naming convention - ClassName
- PascalCase

class Time:
    def __init__(self):
        self.hours = 0
        self.minutes = 0
        
__init__ is a constructor
- this method will be called automatically for every new
instantiation

self sets the "variables" of each instantiation

call --> my_time = Time()
the self is implied
attributes will passed automatically

overwrite
my_time.hours = 69
my_time.minutes = 20

A class is not an object # check this for truth
# - class object?
it is a blueprint for the instantiation of objects
"""

"""
Instance methods are functions defined w/in a class
- referenced using dot notation

# in class
def print_time():
    print('the thing')
    
time_obj.print_time()

__init__ is a special method name
- method that implements some special behavior of the class
"""

"""
class object and instance object

class attribute is shared amongst all of the instances
of that class
"""