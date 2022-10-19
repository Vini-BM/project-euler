# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

qs = 0
sq = 0
for c in range (1, 101):
    sq += c**2
    qs += c
print(sq - qs**2)
