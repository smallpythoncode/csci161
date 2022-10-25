"""
RECURSIVE FUNCTIONS
- functions may call other functions
- it can even call itself, recursion
- not efficient to do a count-down
  - a loop would be better

ord()
- gives the number in the ascii table

Searches via recursive algorithm
guess a number between 1-100
- binary search algos are recursive
  - biforcation (?)
  - same algorithm (split range in half) and reduce range by half
  each time

- base case
  - condition under which recursion stops
- recursion case
  - a call for (further) recursion

Recursive solution can be done using loops

ADDING OUTPUT STATEMENTS FOR DEBUGGING
- debugging recursion can be bear a bear because you have
to keep track of how deep the recursion is
- on trick is to add indentation to detail the current depth
of recursion
- can leave the output statements in the code and comment
them out
  - leaves a record of development
- more advanced technique: logging is part of the Py standard lib

- can set a debug var (bool)
- include if statements to print if debug
- otherwise, it is skipped and the thing just runs

CREATING A RECURSIVE FUNC
0. determine if the problem screams recursion or if it could be done
more efficiently
1. write base case
- every recursive function must have a case that returns a value
w/o performing a recursive call
- may be multiple base cases
2. the programmer adds the recursive case to the function

- cases for recursion are rare in Python
  - according the the author of the textbook

binary trees are very recursive structures

def nfact(n):
    fact = 0
    if n == 1 or n == 0:  # base case
        fact = 1
    return fact


def nfact_fleshed_out(n):
    fact = 0
    if n == 1 or n == 0:  # base case
        fact = 1
    else:
        fact = n * nfact_fleshed_out(n-1)
    return fact

better recursive solution using loop

for i in range(n, 0, -1): result *= i (^factorial#checkme)

Common errors:
- not covering all possible base cases in a recursive func
- write a recursive func that doesn't always reach a base case
  - not adhering to either of these could cause infinite recursion
  - putting in negative number is not 0 or 1
  - -1 will recurse to -2, -3, etc. so

pickup at 39 min mark
"""