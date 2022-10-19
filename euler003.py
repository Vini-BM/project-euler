# The prime factors of 13195 are 5, 7, 13 and 29. What is the largest prime factor of the number 600851475143 ?

from math import sqrt, ceil
primes = []

def isPrime(n):
   if n <= 1 or n % 1 > 0:
      return False
   for c in range(2, int(ceil(sqrt(n))) + 1):
      if n % c == 0:
         return False
   return True

def pFactors(a):
    for i in range(3, int(ceil(sqrt(a))), 2):
        if a % i == 0 and isPrime(i):
            primes.append(i)

num = int(input('Insira um número: '))
pFactors(num)
print(max(primes))
