def isPowerOfThree(n):
    if n < 1:
        return False
    if n == 1:
        return True
    return n % 3 == 0 and isPowerOfThree(n//3)

print(isPowerOfThree(81))
