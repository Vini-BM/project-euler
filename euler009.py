#A Pythagorean triplet is a set of three natural numbers, a < b < c, for which, a^2 + b^2 = c^2
#There exists exactly one Pythagorean triplet for which a + b + c = 1000. Find the product abc.
import numpy as np

def primePythTrips(limit=None):
    u = np.mat(' 1  2  2; -2 -1 -2; 2 2 3')
    a = np.mat(' 1  2  2;  2  1  2; 2 2 3')
    d = np.mat('-1 -2 -2;  2  1  2; 2 2 3')
    uad = np.array([u, a, d])
    m = np.array([3, 4, 5])
    while m.size:
        m = m.reshape(-1, 3)
        if limit:
            m = m[m[:, 2] <= limit]
        yield from m
        m = np.dot(m, uad)

def allPythTrips(limit):
    for prim in primePythTrips(limit):
        i = prim
        for _ in range(limit//prim[2]):
            yield i
            i = i + prim

def checkProd(t, r):
    if t[0] + t[1] + t[2] == r:
        return t[0]*t[1]*t[2]
    else:
        return False

x = list(allPythTrips(10000000))
for q in x:
    q = np.sort(q)
    if checkProd(q, 1000) != False:
        print(checkProd(q, 1000))
        print(q)