"""
Functions
User-defined functions

dynamic typing - polymorhpism - a function's behavior changes based
on the type of argument fed to it
- print('x * 5) --> 'xxxxx'
- doesn't allow mixed types in the same call
  - add(5, '100')

Funcs are cool because they can be stored and used in other programs

As a guideline, a func def shouldn't have more than 30 lines of code

A convention of defining constants is to write its variable in all caps
- CM_PER_INCH = 2.54

FUNCTION STUBS
- if a func is defined, it's body must have some code
- don't want to work on that right now? send 'pass'
  - returns None
- incremental development
- raise a NotImplementedError
  - brings the interpreter to a screeching halt
  - do this if the func is critical to dev

Functions are objects
- has a type, value, identity

COMMON ERRORS
Copy and pasting w/out modifying the code to desired intent

Return error - returning the wrong value or none at all
- don't forget to add a return statement when needed
===

to change the value of global variables, use 'global' statement to
refer to it

good ideas for globals
- data structures that are huge
- when something is speed critical
- legacy variables

globals() & locals() can be used to identify what's in the respective
namespace

pass-by-assignment - arguments to funcs are passed by object reference
- mutable objects will be modified (the actual reference) if called
and modded by a func
- pass a copy to avoid this
"""