"""
LIST COMPREHENSIONS
- do a process to every element in a list
- iterates over a list, modifies each element, returns a new list
containing new list of modified elements
- always surrounded by brackets
- results in less code and can be more efficient in the interpreter

new_list = [expression for loop_var_name in iterable]

conditionals can be implemented to list comprehensions
new_list = [expression for loop_var_name in iterable if condition]

SORTING LISTS
sort() - lowest to highest
- Python uses Tim Sort algo for sort()
  - combo of merge sort and insertion sort

sorted() - creates and return a new list that has been sorted

FUNC VS METHOD
methods are attached to a data objects
- used the data object it is called with as the data to manipulate
function is a stand-alone construct that must be handed data to
manipulate it

keys for sort will view things through a particular lense
- str.lower for example
- key can be any function, not just a method

want it in descending order? flip reverse argument to True

COMMAND-LINE ARGUMENT
- able to type additional things to command line to modify how
the program is run
- can be used to pass arguments from the command line

import sys
name = sys.argv[1]
age = int(sys.argv[2])

- if the wrong number of arguments are passed, an error will be raised

- check if number of arguments passed is equal the num of args
required to run w/o error

if len(sys.argv) != num_required:
    print("you fucked up")

What is argparse? getopt?

DICTIONARIES
dictionary comprehension - similar to list comprehension

dict() is another method for creating a dick
my_dict = {} is the most common method

methods
clear removes all and leaves an empty dict
get reads teh value of the key from a dict
update are used to merge 2 dicts
pop will remove and return a key value

iterating over a dict is done by key

items, keys, and values methods
items returns tuples of key value pairs

list() on dicts converts items for a dict methods into a list

NESTING DICTS
dictionaries can be nested as much as one's heart desires
- a data structure is a method of organizing data in a logical and
coherent fashion

STRING FORMATTING W/ %
print('The couch is %d years old." % couch_age

FORMAT WITH FORMAT()
print('{} burritos cost ${}'.format('6', '2.55')

- double % (%%) actually prints out a percent sign

- ADA is a DoD software
"""