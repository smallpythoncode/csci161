"""
see 20221005 about depth and recursion limits

- 1000 is usually a substantial limit
- all the previous calls are placed into the stack since each layer
is a function call
  - so the system knows the status of previous calls

def rec_func():
    if n == 0:
        return 1
    return rec_func(n-1)

there are some math funcs that do require this level of depth
- can you program things to use the hard drive instead of memory?
- python is not the best for computation in depth
  - other languages manage resources better

RECURSIVE EXPLORATION OF ALL POSSIBILITIES
Recursion is a powerful tool for exploring all possibilities
- such as reordering a word's letters
- all possible subsets of items
- all possible paths between cities

- can be used to give us all the possible combos on a lock

2 parameters
- 1 for the chosen letters
- 1 for the un-chosen letters
"""


def scramble(r_letters, s_letters):
    if len(r_letters) == 0:
        # base case: all letters used
        print(s_letters)
    else:
        # recursive case: for each call to scramble()
        # move a letter from remaining to scrambled
        for i in range(len(r_letters)):
            # the letter at index i will be scrambled
            scramble_letter = r_letters[i]

            # remove letter to scramble from remaining letters list
            # beginning up to i, but no including i --> [:i]
            # excludes i
            # everything up to i and everything after i
            # concatenates and that is remaining_letters
            remaining_letters = r_letters[:i] + r_letters[i+1:]

            # scramble letter
            scramble(remaining_letters, s_letters + scramble_letter)


word = input("Enter a word to scramble: ")
scramble(word, "")

"""
trying to debug recursive functions are a bitch
- when in doubt, write it down
- use debug messages with spaces or * to indicate what level
of recursion it is
- given this, don't use recursion unless you must

what is the enumerate function?????
what is pop() ???

TRAVELING SALESMAN PROBLEM
- blows up the greater the number of cities
- computer will run out of resources before an optimal solution is found
"""
num_cities = 3
city_names = []
distances = []


def travel_paths(curr_path, need_to_visit):
    if len(curr_path) == num_cities:  # base case: visited all cities
        total_distance = 0
        for i in range(len(curr_path)):
            print(city_names[curr_path[i]], " ", end=" ")

            if i > 0:
                total_distance += distances[curr_path[i-1]][curr_path[i]]

        print("=", total_distance)
    else:  # recursive case: travel to each city
        for i in range(len(need_to_visit)):
            # visit city
            city = need_to_visit[i]
            need_to_visit.pop(i)
            curr_path.append(city)

            travel_paths(curr_path, need_to_visit)

            need_to_visit.insert(i, city)
            curr_path.pop()


"""
CHAPTER 15 - PLOTTING

plotting packages are not baked into python but there is a key one available

matplotlib is the microsoft excel of the engineering world
- replicates the plotting capability of MATLAB
- NOTE! also requires the NumPy package


# example
import matplotlib.pyplot as plt

with open("ocean_temp.csv") as temp_file:
    temps = []
    for t in temp_file:
        temps.append(float(t))
        
years = range(1850, 2012)

# years independent axis (x)
# temps dependent axis (y)
plt.plot(years, temps)
plt.show()

STYLING PLOTS
format string argument to specify color and style of plotted line

plt.plot(years, temps, "r--")
# look up this stuff in the docs

format strings are a shortcut to setting line properties
- an attribute of the line object created
# look this up
e.g. alpha, color, antialiased
alpha is transparency
aliasing - raster type graphic system
- dots next to each other, stair stepping effect

ADDING A LEGEND
plt.plot(temp_years, temps, label="Ocean temperature change")
plt.legend(shadow=True, loc="upper right"
"""