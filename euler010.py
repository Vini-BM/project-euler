from is_prime import isPrime

def primeSum(limit):
    sum = 0
    for i in range (1, limit):
        if isPrime(i):
            sum = sum + i
    return sum

print(primeSum(2*10**6))