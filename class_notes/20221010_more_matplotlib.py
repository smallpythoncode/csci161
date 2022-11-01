"""
TEXT AND ANNOTATIONS

text labels can draw attention to interesting parts of a plot

plt.xlabel("year")
plt.ylabel("Number of highway fatalities")
plt.legend(shadow=True, loc="upper right")

plt.title("alcohol related fatalities on highways")

# add text giving x,y coords of the plot
plt.text(1970.5, 11000, "fatalities spike\nin1970s", fontsize=12)

# add a vert line at x-coord 1980
plt.axvline(1980, color="grey")

plt.show()

# matplotlib coords are on data coords, not pixel coords

# https://static-resources.zybooks.com/python/dd_stats.csv

text() function draws a string label on the plot
annotate() creates an annotation that links a text label
w/ a specific data point

arrow_properties = {}
plt.annotate(...arrowprops=arrow_properties)
# what is xy and xytext parameters?

label to display (first arg) is placed at coord described by
xytext

NUMPY
scientific and math computations for python

numpy uses an array data type that is conceptually similar to a list
consisting of an ordered set of elements of the same type

an array can be created using the array() constructor from the numpy
package

multidimensional arrays are created by specifying a list
w/ a tuple of each dimension's elements

creating arrays

import numpy as np

# 1 dimension array
my_array1 = np.array([1, 2, 5 ,6])
# 2 dimension array
my_array2 = np.array([(34, 25), (16, 12)])

heterogeneous - list type
- multiple types of data
homogeneous - only one type of data

sometimes an array must be created before the element values
are known
changing the size of an array is an expensive computation,
so numpy provides functions that create empty pre-sized arrays

zeros() creates an array wih a 0 for every element
ones() uses 1 for every element

the argument to zeros() and ones() is an integer (length)
for a 1 dimensional array or a tuple (row length, column length)
for a 2 dimensional

arrays have to be contiguous in memory
- they have to be one right after the other in memory
- can't be separated

if the size of an array is known beforehand, CREATE IT AS SUCH
- it is labor-intensive otherwise

import numpy as np
zero_array = np.zeros(5)  # 1 dimensional array w/ 5 elements

one_array = np.ones((5, 2))  # 5 rows and 2 elements per row

what is row major?
- stuff is stored by rows
- deals w how 2 dimensional data is stored in single
dimension memory
- python is row major
- one row is input in memory, then the second, etc

common operation is creating a sequence of numbers
- range()

linspace can create a "range" of floats

linspace(0, 1, 11)
starts at 0 and goes to 1
w/ 11 elements
- returns an array

math operations between arrays are performed by the matching elements of each
array

[5 5 5] + [1 2 3] = [6 7 8]

what is dot multiplication?
what is matrix multiplication?

MULTIPLE PLOTS

# like range() for floating point
np.arrange(0.0, 5.0, what_is_this)

fft() ???
what is fast fourier transform?

https://en.wikipedia.org/wiki/Fast_Fourier_transform
# who cares

figure()
- can be used to create multiple figures
- each figure corresponds to a window frame
to be opened by matplot lib


# unique identifiers for each figure
FIGURE1 = 1
FIGURE2 = 2

plt.figure(FIGURE1)
plt.figure(FIGURE2)

what is plt.axis() ???
- used to set the range of the x and y axes

subplot() allows multiple plots to be created in a single figure

plt.subplot(2, 1, 1)
# 2 rows, 1 column, use loc 1

what is plt.tight_layout(pad=1.0)

WARNING matplotlib starts counting at 1
- fucking why?

up next twinx()




"""