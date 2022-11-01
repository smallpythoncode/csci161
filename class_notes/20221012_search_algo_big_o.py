"""
Association of Computing Machinery
- Mason Motschke, president
- keeps computer science students involved in the community
w/ programming, game nights, tutorials/learning sessions,
and other events
- sense of community w/in the CS department
- local chapter ^

- national chapter
- founded in 1947
- world's largest scientific and educational computing society
- headquartered in NYC

meets at 4pm on Fridays
- is this on campus?
- if so, fuck that
- are meetings recorded?
- if not, fuck that

Does Digikey host programming competitions?
companies to look into
- Northrop Grumman
- Fast Enterprises LLC

general email: undacm@gmail.com
president email: mason.motschke@und.edu

am i already on the ACM discord
- sister server, UND help server
- look for QR code from this lecture slide

================================

continuing w/ plotting

twinx()
- x axis units are the same, must
- can use 2 different y-axes

figure = plt.figure()
left_axis = figure.add_subplot(1, 1, 1)  # num cols, num rows, which one we're using
right_axis = left_axis.twinx()

...

left_axis.set_xlabel("Year")
left_axis.set_ylabel("Number of highway fatalities")
right_axis.set_ylabel("% fatalities involving alcohol")


SEARCHING AND SORTING ALGOS
an algorithm si a sequence of steps for accomplishig a task

a linear search is a search algo that starts from the beginning
of a list and checks each element until the search
key is found or the end of list is reached

linear searches are really simple to put into code.

if data set is not sorted, pretty much have to
use the linear search algorithm
- other algos rely on set being ordered

basic linear search will only find the first instance
return -1 is a sentinel value  # not found

algorithm runtime is the time it takes to execute
- he's talking in actual microseconds
- if each comparison takes 1 microsecond
= 1 millions comparisons per second
- equivalent to 1 megahertz processor
  - not very fast
- most computers these days are measured in
gigahertz

searching entire amazon database of
200 million items would take
3 minutes at 1 megahertz

more data in set, longer time to run

at most 32 comparisons for 32 item set
- search all, not found
at best, 1
- insta find

for a list of n elements, linears search thus
requires at most n comparisons
"on the order of" of n comparisons

BINARY SEARCH
because contact list is sorted, a faster search
(binary search) can be used
- checks the middle contact first
- splits each section of comparison by half
each time

binary search is much faster than linear
if search elements are sorted AND each element
is directly accessible
- can go to an arbitrary element number
- linked list
  - a scavenger hunt
  - each element has a clue on how to get to
the next element
- binary is a recursive type of algo

- binary search must be sorted!!!

binary search efficiency?
- how can this be measured?

32 element list
- how many comparisons?
- be halved to 16, 8, 4, etc.
- 6 steps
  - worst case, not found

floor function of log base 2 of N + 1
log(sub)2 N + 1

efficiency of linear is N

average case
- assuming uniform distribution
  - arbitrary location in set
- N over 2, usually
  - N/2
- not worst case

Amazon comparison
- 200M items takes 28 microseconds, 7M times faster than linear

O NOTATION
Big O Notation
- step way from practical and into very mathematical
- a math way of describing how a function
(run time of algo)
generally behaves
in relation to the input size
in big O all funcs that hae the same growth rate
(determined by highest order term of func)
are characterized
using the same big o notation

In essence, all functions that have the same growth rate are considered
equivalent in big O notation

a judge of algo efficiency is how much ram it uses
- if you can just use up more ram, no problem
  - a few extra seconds
- limited ram, you have to more frugal and efficient

- we're not looking at find detail microseconds
- we're looking at ballpark
- one family grows at a much larger rate than another

given a func that describes the run time of algo,
the big o note for that function can be determined using
these rules

1. if f(x) is a sum of several terms, the highest
order term (the one w/ the fastes growth rate)
is kept and others are discarded
2. if f(x) has a term that is a product of several
factors, all constants (those that are not in terms
of x) are omitted

1. weakest link in the chain determines
the strength of the chain

2. what is the most important thing?

algo steps: 5 + 13*N + 7*N^2
big o notation: O(5 + 13*N + 7*N^2) = O(7*N^2) = O(N^2)

- lower order terms grow so slowly that they become
insignificant

You can use an inefficient algorith...
...just be aware of the consequences

is 0.001 really that much more efficient than 0.0001 seconds?

"""