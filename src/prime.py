import math
#brutefoce
def is_prime(n):
    for i in range(2,n):
        if n%i ==0:
            return False
        return True

def isprime(n):
    if n <= 1:
        return False
    if n == 2:
        return False
    if n%2 == 0:
        return False
    m = int(math.sqrt(n))
    for i in range(3, m):
        if n%i == 0:
            return False
    return True

def find_primes(n):
    primes = [True]*(n+1)
    primes[0] = False
    primes[1] = False
    m = int(math.sqrt(n))
    for i in range(2, m):
        if primes[i]:
           for k in (i*i,n):
               primes[k] = False
    return primes

print(is_prime(10))
print(isprime(11))
res = find_primes(20)
print(res, len(res))