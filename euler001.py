# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these
# multiples is 23. Find the sum of all the multiples of 3 or 5 below 1000.

nums = []
var = 1
while var < 1000:
    if var%3 == 0:
        nums.append(var)
        var = var + 1
    elif var%5 == 0:
        nums.append(var)
        var = var + 1
    else:
        var = var + 1
print(sum(nums))
