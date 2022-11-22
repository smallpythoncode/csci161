"""
Quicksort - sorting algo that repeatedly partitions in the input
into low and high parts (each unsorted), then recursively
sorts each of those parts
- to partition the input, quicksort chooses a pivot to divide
the data into low and high parts
- the pivot can be any value w/in the sorted array, commonly
the value of the middle array element

Example: [4, 34, 10, 25, 1]
- everything below and including 10 would go to the left partition
- everything above 10 would go in the right partition
- pivot can be in left, right, or both

Once partitioned, each partition needs to be sorted.

runtime: typically O(N log N) log linear
worst case: O(N^2)

MERGE SORT
- sorting algo that divides the list into two halves, recursively
sorts each half, then merges the sorted halves to produce
a sorted list
- recursive partitioning continues until a list
of 1 element is reached, as a list of 1 element is already sorted
- the magic happens in putting the partitions back together
  - select the smallest part of each of the 2 halves recursively
  as the first element

utilizes a temporary merged list
- as opposed to quicksort which does its sorting in place
- requires twice the amount of memory
  - 2N memory

runtime: O(N log N) log linear
requires O(N) additional memory elements for the temporary
array of merged elements


"""