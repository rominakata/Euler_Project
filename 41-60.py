'''
Problem 41 Pandigital prime
----------
What is the largest n-digit pandigital prime that exists?

Solution
----------
7652413
'''
'''
import time
starttime = time.clock()
from Euler import is_prime, is_pandigital
n = 7654321
while not(is_prime(n) and is_pandigital(n, 7)):
    n -= 2
print n
endtime = time.clock()
print (endtime - starttime)
'''
'''
Problme 42 Coded triangle numbers
----------
How many are triangle words?

Solution
----------
162
'''
'''
import time
starttime = time.clock()
def worth(word): return sum(ord(letter) - ord('A') + 1 for letter in word)

words = open('words.txt').read().replace('"','').split(',')
triangle_numbers = dict.fromkeys(list(n * (n + 1) / 2 for n in xrange(1, 100)),
        1)
print sum(1 for word in words if worth(word) in triangle_numbers)
endtime = time.clock()
print (endtime - starttime)
'''
'''
Problem 43 Sub-string divisibility
----------
Find the sum of all 0 to 9 pandigital numbers with property.

Solution
----------
16695334890
'''
'''
import time
starttime = time.clock()
from Euler import factorial, perm

def check(n):
    s = str(n)
    return int(s[1:4]) % 2 == 0 and int(s[2:5]) % 3 == 0

s = 0
for i in xrange(0, 18):
    a = int(perm(i, '4310') + '952867')
    if check(a): s += a
    a = int(perm(i, '6410') + '357289')
    if check(a): s += a
print s
endtime = time.clock()
print (endtime - starttime)
'''
'''
Problem 44 Pentagon numbers
----------
Find the pair of pentagonal numbers, P_j and P_k, for which their sum and
difference is pentagonal and D = |P_k - P_j| is minimised; what is the value of
D?

Solution
----------
5482660
'''
'''
import time
starttime = time.clock()
def pe44():
    ps = set()
    i = 0
    while True:
        i += 1
        p = (3 * i * i - i) / 2
        ps.add(p)
        for n in ps:
            if p - n in ps and p - 2 * n in ps:
                return p - 2 * n
print pe44()
endtime = time.clock()
print (endtime - starttime)
'''
'''
Problem 45 Triangular, pentagonal, and hexagonal
----------
Find the next triangle number that is also pentagonal and hexagonal.

Solution
----------
1533776805
'''
'''
import time
starttime = time.clock()
p = 165
h = 143
h = 84 * p + 97 * h - 38
print h * (2 * h - 1)
endtime = time.clock()
print (endtime - starttime)
'''
'''
Problem 46 Goldbach's other conjecture
----------
What is the smallest odd composite that cannot be written as the sum of a prime
and twice a square?

Solution
----------
5777
'''
'''
import time
starttime = time.clock()
n = 5
f = 1
primes = set()
while True:
    if all(n % p for p in primes):
        primes.add(n)
    else:
        if not any((n - 2 * i * i) in primes for i in range(1, n)):
            break
    n += 3 - f
    f = -f
print n
endtime = time.clock()
print (endtime - starttime)
'''
'''
Problem 47 Distinct primes factors
----------
Find the first four consecutive integers to have four distinct primes factors.
What is the first of these numbers?

Solution
----------
134043
'''
'''
import time
starttime = time.clock()
from Euler import factor
ci = 1
nf = 4
ns = 4
n = 2 * 3 * 5 * 7
while ci != ns:
    n += 1
    if len(factor(n)) == nf: ci += 1
    else: ci = 0

print n - nf + 1
endtime = time.clock()
print (endtime - starttime)
'''
'''
Problem 48 Self powers
----------
Find the last ten digits of the series, 1^1 + 2^2 + 3^3 + ... + 1000^1000.

Solution
----------
9110846700
'''
'''
import time
starttime = time.clock()
def pe48(limit, m):
    sum = 0
    while limit:
        sum += pow(limit, limit, 10 ** m)
        limit -= 1
    return sum % 10 ** m
print pe48(1000, 10)
endtime = time.clock()
print (endtime - starttime)
'''
'''
Problem 49 Prime permutations
----------
What 12-digit number do you form by concatenating the three terms in this
sequence?

Solution
----------
296962999629
'''
'''
import time
starttime = time.clock()
from Euler import is_prime, is_perm

n = 1489
while True:
    b, c = n + 3330, n + 6660
    if is_prime(n) and is_prime(b) and is_prime(c) \
            and is_perm(n, b) and is_perm(b, c): break
    n += 2
print str(n) + str(b) + str(c)
endtime = time.clock()
print (endtime - starttime)
'''
'''
Problem 50 Consecutive prime sum
----------
Which prime, below one-million, can be written as the sum of the most
consecutive primes?

Solution
----------
997651
'''
'''
import time
starttime = time.clock()
from Euler import prime_sieve, is_prime

max = 1000000
primes = prime_sieve(max)
prime_sum = [0]

sum = 0
count = 0
while (sum < max):
    sum += primes[count]
    prime_sum.append(sum)
    count += 1

terms = 1
for i in range(count):
    for j in range(i + terms, count):
        n = prime_sum[j] - prime_sum[i]
        if (j - i > terms and is_prime(n)):
            (terms, max_prime) = (j - i, n)
print max_prime, terms
endtime = time.clock()
print (endtime - starttime)
'''
'''
Problem 51 Prime digit replacements
----------
Find the smallest prime which, by replacing part of the number (not necessarily
adjacent digits) with the same digit, is part of an eight prime value family.

Soluiton
----------
121313
'''
'''
import time
starttime = time.clock()
from Euler import prime_sieve, is_prime
import string
def eight_prime_family(prime, rd):
    c = 0
    for digit in '0123456789':
        n = int(string.replace(prime, rd, digit))
        if (n > 100000 and is_prime(n)):
            c += 1
    return c == 8

for prime in prime_sieve(1000000):
    if (prime > 100000):
        s = str(prime)
        last_digit = s[5:6]
        if (s.count('0') == 3 and eight_prime_family(s, '0') \
         or s.count('1') == 3 and last_digit != 1 and eight_prime_family(s,'1') \
         or s.count('2') == 3 and eight_prime_family(s, '2')):
            print s
         
endtime = time.clock()
print (endtime - starttime)
'''
'''
Problem 52 Permuted multiples
----------
Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x,
contain the same digits.

Solution
----------
142857
'''
'''
import time
starttime = time.clock()

endtime = time.clock()
print (endtime - starttime)
'''
'''
Problem 53 Combinatoric selections
----------
How many, not necessarily distinct, values of Cnr, for 1 <= n <= 100, are
greater than one-million?

Solution
----------
4075
'''

import time
starttime = time.clock()
from Euler import binomial
limit, maxn, c = 1e6, 100, 0
for n in range(23, maxn + 1):
    for r in range(2, n / 2 + 1):
        if binomial(n, r) > limit:
            c += n + 1 - 2 * r
            break
print c
endtime = time.clock()
print (endtime - starttime)
