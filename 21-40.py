'''
Problem 21 Amicable numbers
----------
Evaluate the sum of all the amicable numbers under 10000.

Solution
----------
31626
'''
'''
import time
starttime = time.clock()
def divisors(n): return list(i for i in xrange(1, n / 2 + 1) if n % i == 0)
pair = dict(((n, sum(divisors(n))) for n in xrange(1, 10000)))
print sum(n for n in xrange(1, 10000) if pair.get(pair[n], 0) == n and pair[n] != n)
endtime = time.clock()
print (endtime - starttime)
'''
'''
Problem 22 Names scores
----------
What is the total of all the name scores in the file?

Solution
----------
871198282
'''
'''
import time
starttime = time.clock()
def worth(name): return sum(ord(letter) - ord('A') + 1 for letter in name)

names = open('names.txt').read().replace('"','').split(',')
names.sort()

print sum((i + 1) * worth(names[i]) for i in xrange(0, len(names)))
endtime = time.clock()
print (endtime - starttime)
'''
'''
Problem 23 Non-abundant sums
----------
Find the sum of all the positive integers which cannot be written as the sum of
two abundant numbers.

Solution
----------
4179871
'''
'''
import time
starttime = time.clock()
from math import sqrt
def d(n):
    s = 1
    t = sqrt(n)
    for i in xrange(2, int(t) + 1):
        if n % i == 0:
            s += i + n / i
    if t == int(t):
        s -= t
    return s

limit = 20162
s = 0
abn = set()
for n in xrange(1, limit):
    if d(n) > n:
        abn.add(n)
    if not any((n - a in abn) for a in abn):
        s += n
print s
endtime = time.clock()
print (endtime - starttime)
'''
'''
Problem 24 lexicographic permutations
----------
What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5,
6, 7, 8 and 9?

Solution
----------
2783915460
'''
'''
import time
starttime = time.clock()
from itertools import permutations
n = []
for i in permutations("0123456789"):
    n.append("".join(i))
print(n[1000000 - 1])
endtime = time.clock()
print (endtime - starttime)
'''
'''
Problem 25 1000-digit Fibonacci number
----------
What is the first term in the Fibonacci sequence to contain 1000 digits?

Solution
----------
4782
'''
'''
import time
starttime = time.clock()
def fibonacci(n):
    a, b = 1, 1
    f = [a, b]
    while len(str(b)) < n:
        a, b = b, a + b
        f.append(b)
    return f
print (len(fibonacci(1000)))
endtime = time.clock()
print (endtime - starttime)
'''
'''
Problem 26 Reciprocal cycles
----------
Find the value of d < 1000 which 1 / d contains the longest recurring cycle in
its decimal fraction part.

Solution
----------
983
'''
'''
import time
starttime = time.clock()
def cycle_length(n):
    i = 1
    if n % 2 == 0: return cycle_length(n / 2)
    if n % 5 == 0: return cycle_length(n / 5)
    while True:
        if (pow(10, i) - 1) % n == 0: return i
        else: i += 1
m, n = 0, 0
for d in xrange(1, 1000):
    c = cycle_length(d)
    if c > m:
        m = c
        n = d
print n
endtime = time.clock()
print (endtime - starttime)
'''
'''
Problem 27 Quadratic primes
----------
Find the product of the coefficients, a and b, for the quadratic expression
that produces the maximum number of primes for consecutive values of n,
starting with n = 0.

Solution
----------
-59231
'''
'''
import time
starttime = time.clock()
import math
from Euler import prime_sieve
def isPrime(n):
    if n <= 1:
        return False
    for i in xrange(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

nmax = 0
a_m, b_m = 0, 0
primes = prime_sieve(1000)
for a in xrange(-999, 999, 2):
    for b in primes:
        n = 1
        while isPrime(n ** 2 + a * n + b): n += 1
        if n > nmax: nmax, p, a_m, b_m = n, a * b, a, b
print a_m, b_m, p
endtime = time.clock()
print (endtime - starttime)
'''
'''
Problem 28 Number spiral diagonals
----------
What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed
in the same way?

Solution
----------
669171001
'''
'''
import time 
starttime = time.clock()
diagonal = 1
start = 1
for width in xrange(3, 1002 , 2):
    increment = width -1
    count = increment * 4
    diagonal = diagonal + start * 4 + increment * 10
    start = start + count
print diagonal
endtime = time.clock()
print (endtime - starttime)
'''
'''
Problem 29 Distinct powers
----------
How many distinct terms are in the sequence generated by a^b for 2 <= a <= 100
and 2 <= b <= 100?

Solution
----------
9183
'''
'''
import time
starttime = time.clock()
terms = {}
count = 0
for a in xrange(2, 101):
    for b in xrange(2, 101):
        c = pow(a, b)
        if not terms.get(c, 0):
            terms[c] = 1
            count = count + 1
print count
endtime= time.clock()
print (endtime - starttime)
'''
'''
Problem 30 Digit fifth powers
----------
Find the sum of all the numbers that can be written as the sum of fifth powers
of their digits.

Solution
----------
443839
'''
'''
import time
starttime = time.clock()
def power_of_digits(n, p):
    s = 0
    while n > 0:
        d = n % 10
        n = n / 10
        s = s + pow(d, p)
    return s

print sum(n for n in xrange(2, 200000) if power_of_digits(n, 5) == n)
endtime = time.clock()
print (endtime - starttime)
'''
'''
Problem 31 Coin sums
----------
How many different ways can 200p be made using any number of coins?

Solution
----------
73682
'''
'''
import time
starttime = time.clock()
target = 200
coins = [1, 2, 5 ,10, 20, 50, 100, 200]
ways = [1] + [0] * target
print len(ways)
for coin in coins:
    for i in xrange(coin, target + 1):
        ways[i] += ways[i - coin]

print ways[target]
endtime = time.clock()
print (endtime - starttime)
'''
'''
Problem 32 Pandigital products
----------
Find the sum of all product whose multiplicand/multiplier/product identity can
be written as 1 through 9 pandigital.

Solution
----------
45228
'''
'''
import time
starttime = time.clock()
from Euler import is_pandigital
p = set()
for i in xrange(2, 100):
    start = 1234
    if i > 9: start = 123
    for j in xrange(start, 10000 / i + 1):
        if is_pandigital(str(i) + str(j) + str(i * j)): p.add(i * j)
print p
print sum(p)
endtime = time.clock()
print (endtime - starttime)
'''
'''
Problem 33 Digit canceling fractions
----------
If the product of these four fractions is given in its lowest common terms,
find the value of the denominator.

Solution
----------
100
'''
'''
import time
starttime = time.clock()
d = 1
for i in xrange(1, 10):
    for j in xrange(1, i):
        for k in xrange(1, j):
            ki = k * 10 + i
            ij = float(i) * 10 + j
            if(k * ij == j * ki):
                print ij, ki
                d *= ij / ki
                print ki / ij
print d
endtime = time.clock()
print (endtime - starttime)
'''
'''
Problem 34 Digit factorials
----------
Find the sum of all numbers which are equal to the sum of the factorial of
their digits.

Solution
----------
40730
'''
'''
import time
starttime = time.clock()
fact = (1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880)
s = 0
for n in xrange(10, 50000):
    x = sum(fact[int(d)] for d in str(n))
    if n == x: 
        s += n
        print n
print s
endtime = time.clock()
print (endtime - starttime)
'''
'''
Problem 35 Circular primes
----------
How many circular primes are there below one million?

Solution
----------
55
'''
'''
import time
starttime = time.clock()
from Euler import prime_sieve, is_prime

def circular(n):
    circ = []
    n = str(n)
    for i in xrange(len(n)):
        circ.append(int(n[1:]+n[0]))
        n = n[1:] + n[0]
    return circ

def is_prime_list(List):
    for i in List:
        if not is_prime(i):
            return False
    return True

primes = prime_sieve(1000000)
circ = []
for i in primes:
    if(is_prime_list(circular(i))):
        circ.append(i)
print len(circ)

endtime = time.clock()
print (endtime - starttime)
'''
'''
Problem 36 Double-base palindromes
----------
Find the sum of all numbers, less than one million, which are palindromic in
base 10 and base 2.

Solution
----------
872187
'''
'''
import time
starttime = time.clock()
from Euler import is_palindromic
dec2bin = lambda n: str(bin(n))[2:]

s = 0
limit = 1000000
for n in xrange(1, limit, 2):
    if is_palindromic(n) and is_palindromic(dec2bin(n)):
        s += n
print s
endtime = time.clock()
print (endtime - starttime)
'''
'''
Problem 37 Truncatable primes
----------
Find the sum of the only eleven primes that are both truncatable from left to
right and right to left.

Solution
----------
748317
'''
'''
import time
starttime = time.clock()
from Euler import is_prime
from math import log10
primes = [23,37,53,73,313,317,373,797,3137,3797,7937,31397,31973,37313,37397,71317,
          71713,71917,73973,79397,313717,317197,319313,371737,371797,373717,373937,
          379397,713737,713917,717317,717397,717917,719197,719713,719717,731713,
          731737,739373,739397,791317,791797,793717,797917]
def trunc(n):
    c = n
    while c > 10:
        c = c % 10 ** (int(log10(c)))
        n = n // 10
        if not is_prime(c) or not is_prime(n): return False
    return True

c, s = 0, 0
for p in primes:
    if trunc(p):
        print p
        c += 1
        s += p
print c, s
endtime = time.clock()
print (endtime - starttime)
'''
'''
Problem 38 Pandigital multiples
----------
What is the largest 1 to 9 pandigital 9-digit number that can be formed as the
concatenated product of an integer with (1, 2, ..., n) where n > 1?

Solution
----------
932718654
'''
'''
import time
starttime = time.clock()
from Euler import is_pandigital
for n in xrange(9876, 9123, -1):
    p = str(n * 1) + str(n * 2)
    if is_pandigital(p):
        print p
        break
endtime = time.clock()
print (endtime - starttime)
'''
'''
Problem 39 Integer right triangles
----------
For which value of p <= 1000, is the number of solutions maximised?

Solution
----------
840
'''
'''
import time
starttime = time.clock()
t_max = 0
p_limit = 1000
for p in xrange(p_limit//2, p_limit + 1, 2):
    t = 0
    for a in xrange(2, p / 4 + 1):
        if p * (p - 2 * a) % (2 * (p - a)) == 0: t += 1
        if t > t_max: (t_max, p_max) = (t, p)
print p_max
endtime = time.clock()
print (endtime - starttime)
'''
'''
Problem 40 Champernowne's constant
----------
Solution
----------
3920
'''
'''
import time
starttime = time.clock()
n ,c = 0, '.'
while (len(c) <= 1000000):
    n += 1
    c += str(n)
print int(c[100]) * int(c[1000]) * int(c[10000]) * int(c[100000]) * int(c[1000000])   
print c[100],c[1000],c[10000],c[100000],c[1000000]
endtime = time.clock()
print (endtime - starttime)
'''