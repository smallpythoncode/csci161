"""
CHAPTER 13 - Derived classes

A class will commonly share attributes w/ another class but w/ some
additions and variations

class Fruit might be derived from class Item w/ an expiration date
added

class Item:
    def __init__(self):
        self.name = ''
        self.quantity = 0

class Produce(Item): # derived from Item
    def __init__(self):
        Item.__init__.self # call base class constructor
        self.expiration = ''

    def set_expiration(self, expir):
        self.expiration = expir

item1 = Item()
item1.set_name('Booty-Os')

item2 = Produce()
item2.set_name('Apples') # available to Produce via Item
item2.set_expiration('Dec 25, 2022')

derived class refers to a class that inherits that the class
attributes are of another class known as a base class
- inheritance

inheritance relationships are commonly depicted using Unified
Modeling Language notation

− private
+ public
# protected

This shit will be covered in future classes
- Dr. Grant
- writing software in an engineering-minded way
- waterfall method
  - designing the code (diagrams, documentation) before any code
  is actually written
  - avoids rewrites of code, pre-approved by customers

Extreme programming
- writing code right away knowing that most of it will be thrown away

a derived class can serve as a base class for another derived class
- can have multiple derivations
a class may be derived from multiple classes
- class House(Dwelling, Property)

ACCESSING BASE CLASS ATTRIBUTES
Attribute reference order:
1. the instance's namespace
2. the classes' namespace
3. the namespace of any base classes

OVERRIDING CLASS METHODS
a derived class may define a method that overrides the method
of the same name in the base class

# base
def deez_nuts():
    print('got eem')
# derived
derived deez_nuts():
    print('did something come in the mail?)

if a derived class called the deez method, a mail question would
be posed

A programmer will often want to extend rather than replace
the base class method
call the method from the derived class and add functionality

Is-a vs. has-a relationships !!!
inheritance vs composition
first, derived
second, one object may be made up of other objects

class Mother may have a list of class Child objects attributed to it

'is-a' = inheritance

MIXIN CLASSES AND MULTIPLE INHERITANCE
M.I.
- derived from multiple base classes

mixins are classes that provide some addition behavior by mixing in
new methods but are not themselves meant to be instantiated
- meant to be used to create base functionality so other classes
can be derived and use those new methods

UNITTEST MODULE
- testing individual portions of software
end-to-end tests whole package rather than individual units

unittest runs assertions








"""