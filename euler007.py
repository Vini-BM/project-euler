#By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
# What is the 10 001st prime number?

from math import ceil, sqrt

def isPrime(n):
   if n <= 1 or n % 1 > 0:
      return False
   if n == 2:
       return True
   for c in range(2, int(ceil(sqrt(n))) + 1):
      if n % c == 0:
         return False
   return True

primes = [2]
i = 3
while len(primes) < 10001:
    if isPrime(i):
        primes.append(i)
        i+=2
    else:
        i+=2
print(max(primes))
