"""
Chpt 12
Files

open() function opens a file (no shit) to retrieve its data

some_file = open('filename.txt', 'mode')
contents = some_file.read()

file.close() closes the file (no shit), after which no more
reads or writes to files are allowed

take care of carriage returns/line carries when working w/ .txt files
- copy and pasting doesn't always translate well if, say, one
copies text from web page

file object

f = open('filename.txt')
- if no filepath, the interpreter expects the file to be in the same
dir from which it's being called, the .py

contents = f.read() # read file text into a string
f.close() # close the file
print(contents)

file.read() returns the file contents as a string
file.readlines() method returns a list of strings, where the first
element is the contents of the first line, the second the second line,
etc.

linux and mac use forward slashes

it is good practice to close files after writing in case
there are multiple writer programs which may corrupt the file

file.readline() returns a single line at a time, which is useful
when dealing w/ large file where the entire file contents
may not fit into the available system memory

both read and readlines can be given an optional argument
that specifies the number of bytes to read from the file
- handy for huge files and one only wants a certain amount
of data

WRITING FILES

file.write() writes a string argument to a file
- method accepts string args only
- ints and floats must first be converted using str()

writing has no implied return character
- must specify an r char (\n) otherwise all data the succeeds
it for writing will be at the end of what was just written

Modes for opening files:
r - reading
w - writing
a - append

what is r+? what am + for mode?
- update mode
  - both reading and writing at the same time
  - do more research as there are questions on where the pointer is in
  this mode
  - worth learning as it allows for more advanced file manipulation

buffering can be toggled on/off or a buffer size can be specified
f = open('deez_nuts.txt', 'w', buffering=100)
- buffer to disk every 100 bytes
- 0 disables buffering
- may only work for binary files

flush() file method can be called to force the interpreter to flush
the output buffer to disk
- alternate on some systems is os.fsync()

INTERACTING WITH FILE SYSTEMS
os module provides an interface to OS

os.stat() - what is?
- checks the status of a file

An os doesn't actually delete anything...
- this is done for performance's sake
- also allows retrieval in the case of an oopsie
...it just marks that space in disk space as no longer in use

portability and path separators
os.path.join() concatenates arguments suing the correct path sep for
the current os

path = os.path.join('subdir', 'bat_mobile.jpg')
results in "subdir\\bat_mobile.jpg" on Windows
"subdir/bat_mobile.jpg" on Linux/Mac

inverse, splitting a path into tokens
tokens = 'C:\\Users\\BWayne\\tax_return.txt'.split(os.path.sep)
- puts the tokens into a list
"""