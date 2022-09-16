"""
***STRINGS***

STRINGS SLICING
- mystr[start:end]
- the last character (end) is one location before the specified end
  - use desired end + 1 if it makes it more readable
- mystr[:-2] to calc backwards
   - this case, second to last character
   - [:-1] all but last character

slicing and slice operation creates a copy
- leave the original unharmed

can omit values
- [:end] assumes start at index 0

[start:end:stride] - how many to skip
...:2] does every other character

ADVANCED STRING FORMATTING
field width
- f'{name:16}
  - 16 is the number of characters available to print name
  - indexes 0 through 15 (if at the start)
  - defaults to left align

alignment character
<, >, ^ is left, right, and center aligned respectively
- {name:>16} is right aligned

fill character - fills what would be empty space
- {name:.>16} fills empty space w/ dots

floating point precision
- {0.69420:.2f} will only print '0.69'
- python rounds floating point nums
  - c simply truncates

STRING METHODS
replace(old, new) - returns a copy of the string
- doesn't change the original string
- applies to all instances
  - to apply to only a specific number, use count parameter
    - replace(old, new, count)

find(x) looks for first instance of x by index
find(x, start)
find(x, start, end)
rfind(x) - same but in reverse
count('oo') counts the number of instances of 'oo'

can use relational operators
- compares by unicode character
can use equality operators
- ==, !=
membership
- in, not in
identity (looks for instances in memory)
- is, is not

capitalize, lower, upper, strip, title
strip returns a copy with leading and trailing whitespace removed
title returns a copy with first letters of words capitalized

SPLIT METHOD
- tokens are parts of a larger string
- the separator is the character of sequence of characters that
indicate where to split the strings into tokens
- returns a list of tokens

JOIN METHOD
- opposite of split
- concatenates the elements of a list of strings
- my_str = '@'.join(['billgates', 'microsoft']

LISTS
append, extend, insert methods for adding
remove, pop for removing
sort, reverse() for modifying
misc: index, count

mind IndexError when trying to access a list element with an index
specified outside the range of the list
- buffer overflow attacks

ENUMERATE
iterates over a list and provides and interation counter

any, all, max, list, sum

list nesting
- putting lists inside of lists
- allows for multi-dimensional data structures

nested loops
- typically the number of layers is equal to the number of dimensions
of the list
  - if 2 dimensions, 2 loop layers

LIST SLICING
my_list[0:2]

iterating over lists
for i in range(len(my_list)):
    ...

copy a list
- my_list[:]

"""