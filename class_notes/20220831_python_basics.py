"""
string literal is a string specified in the source code

empty string has 0 elements
len() used to measure length of string

input function only returns strings

indexing can be used with negative nums
indexing - [] in string variable

why does the index start at 0?
- specifying an element number is an offset of where the element
  is in memory

  - specifying 0 points directly to where the element is stored
  - specifying 2 points to where the elements starts then adds 2
  - -10 starts at the end and goes back 10
    - in C, it would enter the memory space of a different element

strings are immutable
- individual elements of a string cannot be modified after assignment02
- the entire variable must be re-assigned
- can also slice parts of a string and concatenate them

string concatenation
- "string" + "other string"

list
- Swiss army knife of Python
- container
  - sequence type
- heterogeneous
  - can store any type of object, can be mixed

pop(i) - removes element at index i
- no element specified removes a random element...but why?
remove(j) - removes the first element whose value is j

Tuples - immutable list
- what is a named tuple?
  - from collections import namedtuple
  - mashup of tuple, dict, and class

sets - unordered collection of unique elements
nums1 = set([1, 2, 3])
nums2 = { 4, 5, 6 }
  - be careful, same as dict
- removes duplicates at run

dicts
- mini databases
- key:value pairs
  - values can be any type, even other dictionaries
- add pair
  - dict['key'] = 420.69
- keys must be unique

equality operator - ==
inequality op. - !=

computers represent floats as approximations
- use threshold values to see if something is "close enough" if that is the
goal
- floating point numbers should not be compared using equality operators
  - approximation

membership operator - in
- in only checks keys for dicts
  - to check values, you must create list of values ( probably values() method)

identity operator
- not same as equality operator
- checks if two variables are the same objects
- checks whether two operands are bound to a single object
- relates only to objects!!!!!
- x is y is a comparison equivalent to id(x) == id(y)
"""