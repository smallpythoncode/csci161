"""
Big O complexities

common big o complexities
- the best algo is one that has a constant time complexity
- unfortunately, not all problems can be solved using constant
complexity algos
- in fact in many cases, comp scientists
have proven that certain types of problems can only be
solved using quadratic or exponential algos

# image 20221014_runtime_complex_1
# image 20221014_runtime_complex_2
# image 20221014_runtime_complex_3

ALGO ANALYSIS
To analyze how runtime of an algo scales as the input size increases,
we first determine how many ops the algo executes for a specific
input size, N
Then, the big-O notation for that func is determined
Algo runtime analysis often focuses on the worst-case runtime
complexity.
- the runtime complexity for an input that results in the longest
execution
- other analyses include best-case and average-case
  - average requires knowledge of the statistical properties
  of the expected data inputs
- analysis mainly focuses on worst-case
  - most resources, including customer angst

# 20221014_calculating_big_o
4. The function f(N) specifies the number of ops executed for input
size N. The big-O notations for the func is the algo's worst
case runtime complex

# 20221014_constant_time_ops
# 20221014_runtime_analysis_nested_loop

INTRO TO SORTING
- a big deal in computer and data science

sort() list method
sorted() builtin function
- Python uses tim sort for these
  - a hybrid of 2 different algos

selection sort treats the input as two parts, a sorted part
and an unsorted part, and repeatedly selects the proper next value
to move from the unsorted part to the end of the sorted part

# 20221014_selection_sort

bubble sort, look it up
- really simple to code but increasingly inefficient
as set size increases
- poor real-world performance, mainly an education sort
- timsort, look it up

# 20221014_insertion_sort

a nearly sorted list only contains a few elements
not in sorted order

NEXT: quicksort


"""