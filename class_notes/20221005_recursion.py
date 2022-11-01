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

do we do the error checking inside the function or where it is called?
- inside the func is more robust
- waste of processing time
- use of func properly, it is a moot point

- better at call
- only done once
- if loaded into a library, the user must read the docs
  - rage for not rtfm

commonly, programmers will use 2 funcs for recursion
- an outer function to be called from other parts
- an inner function is intended only to be called from that outer
  - leading _ to indicate not intended for user call
- outer func more intuitive
  - user only interacts with outer, fine details in inner

RECURSIVE MATH FUNCS
- fibonacci sequence
0 1 1 2 3 5 8 13 21 34

compute for a specific number of times

def fibonacci(v1, v2, run_cnt):
    print(v1, "+", v2, "=", v1+v2)

    if run_cnt <=1:  # base case
                     # ran for user's number of steps
        pass  # Do nothing
    else:  # Recursive case
        fibonacci(v2, v1+v2, run_cnt-1)

why is fibonacci interesting?
- golden ratio
- golden spiral
- show up in nature
- some parts of human body
- drives numerologists nuts
- popular in study of aesthetics

subscribe to fibonacci quarterly, magazine

recursion can be used to calculate the greatest common divisor
solution calculation
- what is the largest number that is divisible by 2 nums
- see Euclid, 300 BC

def gcd(n1, n2):
    if n1 % n2 == 0:  # n2 is a common factor
        return n2
    else:
        return gcd(n2, n1%n2)

the depth of recursion is measure of how many recursive calls of a func
that have been made, but have not yet returned
each recursive call requires the Python interpret to allocate more
memory, and eventually all system memory could be used
thus, a recursion depth limit exists, accessible using the func
sys.getrecursionlimit()
the default depth limit is typically 1000.
the limit can be changed using sys.setrecursionlimit()
exceeding the depth limit causes RuntimeError to occur
"""