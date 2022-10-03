"""

4 of 4,158
161 Notes 20220926
Inbox

JAHNKE, KENNETH W TSgt USAF ANG 119 ISS/OST
Attachments
12:28 PM (8 hours ago)
to me





Cheers,



TSgt Jahnke

119 ISS/OST

Comm:   701-451-2956

DSN:    312-362-8956

VOSIP:  302-265-0627

TSVOIP: 557-2391

NIPR:   kenneth.jahnke@us.af.mil

SIPR:   kenneth.w.jahnke.mil@mail.smil.smil

JWICS:  kenneth.jahnke@af.ic.gov







Attachments area
11.1 MODULES
Script - .py file passed to the interpreter as input
- lost if written in the interactive interpreter
Module - .py file containing code that can be imported and used by scripts,
other modules, or the interactive interpreter

the import statement calls the module file name
- the .py is assumed
- w/in the same library or w/in the PATH
  - if not in these, a filepath can be specified

module names are case sensitive
- import ABC is different from import abc

Dependency - a module required by another program

Good practice is to place import statements at the top of the file
- not necessary

A dict of the loaded modules is stored in sys.modules

A module object is simply a namespace that contains defs in the module
- if two imported with name some_func, one can be specified with
as keyword
  - this note need more elaboration

The address var of HTTPServer can be accessed as
HTTPServer.address
can be overwritten
HTTPSServer.address = "www.yahoo.com"

FINDING MODULES
1. looks for built-in modules first
- e.g. math, sys
2. Searches the list of directories contained by sys.path
- located in the sys module

The sys.path variable initially contains the following directories:
1. The directory of the executing script
2. A list of directories specified by the environment variable PYTHONPATH
- likely virtenv
- unlikely global
3. The directory where Python is installed

A programmer might set the environment variable PYTHONPATH in the OS
An env var is much like a var in a Py script, except that an env var is stored
by the comp's OS and can be accessed by every program running on the comp

In Windows, a user can set the value of PYTHONPATH permanently through
the control panel, or temporarily on a single instance of a command
terminal (cmd.exe) using the command set PYTHONPATH="c:\dir1;c:\other\directory"
- the ; denotes 2 different paths

IMPORT SPECIFIC THINGS FROM A MODULE RATHER THAN THE WHOLE THING
from module_name import func1, func2, var1

from module_name import *
- imports everything into the global namespace
- not advised unless you are familiar w/ the module to avoid namespace collisions

hashlib module - standard library module tha contains a number of algos for creating
as secure hash of a text message

EXECUTING MODULES AS SCRIPTS


implement this to allow you to run it as a script
yet still keep the functionality as a module
"""
def main():
    pass # stand-in

if __name__ == "__main__":
    main()
"""

urllib - a fun module for grabbing stuff from the web

RELOADING MODULES
reload()
- usually only helpful for things that are running for a long time
such as a web server
- if a module is changed during runtime, one can reload it
to account for those changes

import smtplib
from email.mime.text import MIMEText

mod_time = os.path.getmtime(send.gmail.__file__)
- send_gmail is custom

__file__ contains the path toa module in the comp file system

At UND, 99% of email is spam

PACKAGES
- a directory that when imported, gives access to all the modules w/in that directory
- to indicate that a directory is a package, a __init__.py file must be w/in
  - can be empty
  - can add functionality, such as imports, versioning, etc
"""