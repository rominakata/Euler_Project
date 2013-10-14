'''
Problem 61 Cyclical figurate numbers
----------
Find the sum of the only ordered set of six cyclic 4-digit numbers for which
each polygonal type: triangle, square, pentagonal, hexagonal, heptagonal, and
octagonal, is represented by a different number in the set.

Solution
----------
28684
'''
'''
import time
starttime = time.clock()

def fn(n):
    return (3, n*(n+1)/2), (4, n*n), (5, n*(3*n-1)/2), (6, n*(2*n-1)), (7,
            n*(5*n-3)/2), (8, n*(3*n-2))

def next(types, data): 
    if len(types) == 6 and data[0]//100 == data[-1]%100:
        print data, sum(data)
    else:
        for t, n in ds.get((types[-1], data[-1]), []):
            if t not in types:
                next(types + [t], data + [n])

p = []
n = 19 #first n for octogonal number > 999

while n < 141: #last n for triangle numbers < 10000
    for type, data in fn(n):
        if 1000 <= data <= 9999 and data%100 > 9:
            p.append((type, data))
    n += 1

ds = {}
for t1, d1 in p:
    for t2, d2 in p:
        if t1 != t2 and d1%100 == d2//100:
            ds[t1, d1] = ds.get((t1, d1), []) + [(t2, d2)]

for type, data in ds: next([type], [data])

endtime = time.clock()
print (endtime - starttime)
'''
'''
Problem 62 Cubic permutations
----------
Find the smallest cube for which exactly five permutations of its digits are
cube.

Solution
----------
127035954683
'''
from collections import defaultdict
import time
starttime = time.clock()

def cube(x): return x**3;

def main():
    cubes = defaultdict(list)
    for i in range(10000):
        c = cube(i)
        digits = ''.join(sorted([d for d in str(c)]))
        cubes[digits].append(c)
    print min([min(v) for k, v in cubes.items() if len(v) == 5])

if __name__ == "__main__":
    main()

endtime = time.clock()
print (endtime - starttime)
