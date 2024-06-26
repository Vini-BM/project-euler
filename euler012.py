# The sequence of triangle numbers is generated by adding the natural numbers.
# So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. The first ten terms would be:
# 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...
# Let us list the factors of the first seven triangle numbers:
# 
#      1: 1
#      3: 1,3
#      6: 1,2,3,6
#     10: 1,2,5,10
#     15: 1,3,5,15
#     21: 1,3,7,21
#     28: 1,2,4,7,14,28
# 
# We can see that 28 is the first triangle number to have over five divisors.
# What is the value of the first triangle number to have over five hundred divisors?

from functions import nth_triangle_number, numFactors, factors

n = 1 # initial guess
num_factors = 1

#print(factors(10000))

while num_factors <= 500:
    triangNum = nth_triangle_number(n)
    tn_factors = factors(triangNum)
    num_factors = len(tn_factors)
    print(n,triangNum,num_factors)
    #print(tn_factors)
    n += 1

print('-----------')
