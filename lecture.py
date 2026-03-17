# PART 1
def is_palindrome(s):
    # Check if a string is a palindrome or not.
    # To make it simple, let's assume that an empty string is a palindrome.

    if len(s) <= 1:
        return True  # base case 1
    else:
        for i in range(0, len(s)):
            if s[i] != s[-(i+1)]:
                return False
        return True

    # TODO: test_palindrome_long() will trigger RecursionError. Can you fix it by rewriting the above code?
    # HINT: You can use a loop to replace the recursive call.
    # TODO: How do you check if your fix is correct?


# PART 2
def is_small(a):
    if a < 5:
        return True
    else:
        return False

def randomised_function():
    from random import randint
    a = randint(0, 10)

    if is_small(a):
        return 'software'
    else:
        return 'engineering'


# PART 3 (Advanced Topic)
def difficult_function(x, y):
    if complex_math(x, y) < 0.000001:
        return 'solved!'  ## TODO: How can we cover this line? In other words, how to find (x, y) that makes this line executed?
    else:
        return 'not yet'


def complex_math(x, y):
    import numpy as np
    a = 20
    b = 0.2
    c = 2 * np.pi
    t1 = -a * np.exp(-b * np.sqrt(0.5 * ((x-10) ** 2 + y ** 2)))
    t2 = -np.exp(0.5 * (np.cos(c * (x-10)) + np.cos(c * y)))
    return t1 + t2 + a + np.e

if __name__ == '__main__':
    print(difficult_function(10, 0))