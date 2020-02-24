import datetime
import sys

# basic method
def find_gcd1(a, b):
    fact_a = []
    fact_b = []
    for i in range(1, a+1):
        if a%i == 0:
            fact_a.append(i)
    for i in range(1, b+1):
        if b%i == 0:
            fact_b.append(i)
    result = [value for value in fact_a if value in fact_b]
    return result[-1]

# optimized with while loop while iterating from min value backward and 1.
# e.g (8,12) - start from 8 and go reverse till 1. But grab the one with latest factor.
def find_gcd(a, b):
    i = min(a,b)
    while i>0:
        if a%i == 0 and b%i == 0:
            return i
        else:
            i = i-1

# most optimized one with Euclid's algorithm using recursion.
# let m = ad, n = bd (a,b are factors) ; here m>n
# m-n = ad-bd = (a-b)d .. here d divides both (m-n) as well.
# ** If d divides both m,n it also divides (m-n). Here d is the largest divisor.
# So gcd(m,n) = gcd(n, m-n)..

def gcd_recursion(m,n):
    if m< n:
        (m,n) = (n,m)
    if (m%n) == 0:
        return n
    else:
        diff = m-n
        return gcd_recursion(n, diff)

x = 8110000
y = 1222000
# m = datetime.datetime.now()
# print find_gcd(x, y)
# b = datetime.datetime.now()
# print(b-a)
# print(".................")

c = datetime.datetime.now()
print gcd_recursion(x, y)
d = datetime.datetime.now()
print(d-c)
