"""
What is the difference between sys and os libraries?

CLASS CUSTOMIZATION

# in class
def __str__(self):
    return f"{var} is badass"

print(object)
--> suicide is badass

OPERATOR OVERLOADING
customize the functionality of built-in operators (<, >, +, etc.)

# less than
def __lt__(self, other):

__lt__ is a rich comparison method
"""

"""
9.9 Classes as numeric types

to handle errors resulting from comparison of different types, use 
isinstance()
"""

"""
MEMORY ALLOCATION AND GARBAGE COLLECTION
mem all - the process of an application requesting adn being
granted memory
- Python does this automatically
  - compared to C which handles this manually
- done by the OS, not the interpreter

Most OS don't hand out mem byte by byte
they typically hand out in blocks or chunks

When an object is no longer referenced by any variables,
the object becomes a candidate for de-allocation

A reference count is an integer counter that represents
how many variables reference an object
When an object's reference count is 0, that object
is no longer referenced
- Python will de-allocate objects w/ a reference count
of 0

What is a memory leak?

Memory leaks in a web server are very bad
"""