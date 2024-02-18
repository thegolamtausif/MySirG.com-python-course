s=set(eval(input("Enter the values of your set -" )))
p=set()
ps=set()
n=len(s)
for j in range (n):
   for i in s:
     p.add(i)
     print(p)
   s.pop()
   p.clear()

"""
import itertools
def power_set(s):
    s = list(s) 
    return itertools.chain.from_iterable(itertools.combinations(s, r) for r in range(len(s) + 1))
s =set(eval(input("enter the value of set - ")))
print([set(subset) for subset in power_set(s)])
"""