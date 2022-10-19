# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is
# 9009 = 91 × 99. Find the largest palindrome made from the product of two 3-digit numbers.


def isPalindrome(x):
    if x [::-1] == x:
        return True
    else:
        return False

list = []
for c in range (100, 1000):
    for i in range (100, 1000):
        x = c * i
        if isPalindrome(str(x)):
            list.append(x)
print(max(list))
