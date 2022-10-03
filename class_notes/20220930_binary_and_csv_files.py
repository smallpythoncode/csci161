"""
Interacting w/ file systems
- os modules
  - path separators

os.path.join
os.path.sep

os.path.join('C:\\', 'subdir1', 'myfile.txt')
- drive letters are not supported in Mac/Linux

use split(os.path.sep)
- will split along the separation character

os.path.exists
os.path.isfile
os.path.getsize
os.path.split
- splits a path into a 2-tuple
- tail is the last token in the path
- head is everything else

A programmer may want to check every file and/or subdir
of a specific part of the file system
- os.walk() walks a dir tree, visits each subdir
- 3-tuple --> dir, subdir, files
- recursive

BINARY DATA
bytes()
- bytes('A text string', 'ascii') creates a sequence of bytes by
encoding the string using ASCII
- bytes(100) creates a sequence of 100 bytes whose values are all 0
- bytes([12, 15, 20]) - creates a sequence of 3 bytes with values
from the list

bytes literal
b'some string'

\x escape character preceding the hexadecimal value that describes
the value of the byte

binary file mode
- open('myfile.txt', 'rb')
- on Windows, \n are not automatically mapped to Windows format \r\n

.bmp is a bitmap
- not compressed

what is the struct module?
- packing values into sequences of bytes
- unpacks sequences of bytes into values
struct.pack('>h', 5)
what the fuck is endian?
big-endian?
- '>' places the most significant byte first (big-endian)
- '<' will place the least significant first
'h' describes the value being converted as a 2-byte integer
- other common chars are 'b' for 1-byte, 'l' for 4-byte

COMMAND-LINE ARGUMENTS AND FILES

THE 'WITH' STATEMENT
can be used to open a file, execute a block of statements, and auto
close the file when complete

with open('some_file.txt', 'r') as sf:
    # some bull shit
- context manager
  - manages the use of a resource

CSV FILES
separates data items called fields by comma characters
- not limited to commas, delimiter can be specified
- first line is the legend typically

csv module
- creates a reader object which acts like a container

with open('csv_bs.csv', 'r') as csvfile:
    grades = csv.reader(csvfile, delimiter=',')

can also write w/ grades = csv.writer(csvfile)
"""