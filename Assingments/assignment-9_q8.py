# import the itertools module
import itertools

# define a function to print all subsets of r elements from a set of n elements
def print_subsets(s, r):
    # convert the set to a list
    s = list(s)
    # use combinations to create an iterator of all possible subsets of r elements
    subsets = itertools.combinations(s, r)
    # iterate through the subsets and print them as sets
    for subset in subsets:
        print(set(subset))

# test the function with an example set and value of r
s = {1, 2, 3, 4, 5, 6, 7, 8, 9, 0}
r = 5

print_subsets(s, r)
