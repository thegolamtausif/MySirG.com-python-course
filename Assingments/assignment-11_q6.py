import itertools
def pco(s):
    n=2
    s = list(s)
    subsets = itertools.combinations(s, n)
    return subsets
s = {1, 2, 3}
x=pco(s)
for subset in x:
        print(set(subset))