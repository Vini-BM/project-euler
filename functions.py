import numpy as np
from math import ceil, floor, sqrt, gcd

def digit_sum(num):
    str_num = str(num)
    summation = 0
    for character in str_num:
        summation += int(character)
    return summation

def factorial(n, stop=0):
    fact = 1
    while n>stop:
        fact *= n
        n -= 1
    return fact

def collatz_sequence_len(n, len_dict):
    '''
    Returns the length of the Collatz sequence for starting value n.
    len_dict is the global dictionary with n : sequence length.
    '''
    if n in len_dict:
        return len_dict[n]
    else:
        if n == 1:
            len_dict[n] = 1
        if n%2==0:
            len_dict[n] = 1 + collatz_sequence_len(n/2,len_dict)
        else:
            len_dict[n] = 2 + collatz_sequence_len((3*n+1)/2,len_dict)
    return len_dict[n]

def square_adjacency_matrix(L):
    N = L**2
    matrix = np.zeros((N,N))
    for i in range(N):
        # First row:
        if i <= L-1:
            # All columns:
            matrix[i][i+L] = 1 # down neighbor
            # First column:
            if i % L == 0:
                matrix[i][i+1] = 1 # right neighbor
            # Last column:
            elif i % L == L-1:
                matrix[i][i-1] = 1 # left neighbor
            # Remaining columns:
            else:
                matrix[i][i+1] = 1 # right neighbor
                matrix[i][i-1] = 1 # left neighbor
        # Last row:
        elif i >= N-L:
            # All columns:
            matrix[i][i-L] = 1 # up neighbor
            # First column:
            if i % L == 0:
                matrix[i][i+1] = 1 # right neighbor
            # Last column:
            elif i % L == L-1:
                matrix[i][i-1] = 1 # left neighbor
            # Remaining columns:
            else:
                matrix[i][i+1] = 1 # right neighbor
                matrix[i][i-1] = 1 # left neighbor
        # Remaining rows:
        else:
            matrix[i][i-L] = 1 # up neighbor
            matrix[i][i+L] = 1 # down neighbor
            # First column:
            if i % L == 0:
                matrix[i][i+1] = 1 # right neighbor
            # Last column:
            elif i % L == L-1:
                matrix[i][i-1] = 1 # left neighbor
            # Remaining columns:
            else:
                matrix[i][i+1] = 1 # right neighbor
                matrix[i][i-1] = 1 # left neighbor
    return matrix

def count_grid_routes(n):
    num_routes = 1
    for i in range(1,n+1):
        num_routes *= (n+i)/i
    return num_routes

def nth_triangle_number(n):
    """
    Returns the nth triangular number
    """
    return (n**2+n)/2

def factors(n):
    """
    Returns the list of factors of an integer n
    """
    factors = [1,n] # start list of factors 
    for i in range(2, ceil(np.sqrt(n)+1)): # loop from 2 to sqrt(n)
        if n%i == 0: # if i is a divisor
            factors.append(i) # append i
            if n//i != i: # if i is not sqrt(n)
                factors.append(n//i) # append n//i, which is also a divisor
    factors.sort() # sort for convenience
    return factors

def numFactors(n, len_dict):
    '''
    Returns the number of factors of n
    len_dict is the global dictionary n : number of factors
    '''
    if n in len_dict:
        return len_dict[n]
    else:
        if n == 1:
            len_dict[n] = 1
        else:
            len_dict[n] = len(factors(n))
    return len_dict[n]

def pollardsRho(g,c,n,x0=2):
    '''
    Pollard's Rho factorization algorithm
    g(x,c) is the polynomial mod n
    n is the number to factorize
    Returns a non trivial factor of n
    '''
    t, h = x0, x0
    d = 1
    while d == 1:
        t = g(t,c) % n
        h = g(g(h,c),c) % n
        d = gcd(abs(t-h),n)
    if d == n:
        return
    else:
        return d