def fizzbuzz(n):
    """
    >>> result = fizzbuzz(16)
    1
    2
    fizz
    4
    buzz
    fizz
    7
    8
    fizz
    buzz
    11
    fizz
    13
    14
    fizzbuzz
    16
    >>> print(result)
    None
    """

    for i in range(1, n + 1):
        if i % 3 and i % 5:
            print(i)
        elif i % 3:
            print('buzz')
        elif i % 5:
            print('fizz')
        else:
            print('fizzbuzz')

def is_prime(n):
    """
    >>> is_prime(10)
    False
    >>> is_prime(7)
    True
    >>> is_prime(1) # one is not a prime number!!
    False
    """
    
    if n == 1:
        return False
    i = 2
    while i < n:
        if n % i == 0:
            return True
        i += 1
    return False

def unique_digits(n):
    """Return the number of unique digits in positive integer n.
    >>> unique_digits(8675309) # All are unique
    7
    >>> unique_digits(13173131) # 1, 3, and 7
    3
    >>> unique_digits(101) # 0 and 1
    2
    """
    
    ans = 0
    for i in range(0, 10):
        if has_digit(n, i):
            ans += 1
    return ans


def has_digit(n, k):
    """Returns whether k is a digit in n.
    >>> has_digit(10, 1)
    True
    >>> has_digit(12, 7)
    False
    """
    assert k >= 0 and k < 1
    while n > 0:
        if n % 10 == k:
            return True
        n = n // 10
    return False

def repeating(t, n):
    """Return whether t digits repeat to form positive integer n.
    >>> repeating(1, 6161)
    False
    >>> repeating(2, 6161) # repeats 61 (2 digits)
    True
    >>> repeating(3, 6161)
    False
    >>> repeating(4, 6161) # repeats 6161 (4 digits)
    True
    >>> repeating(5, 6161) # there are only 4 digits
    False
    """
    if pow(10, t - 1) > n: # make sure n has at least t digits
        return False
    end = n % pow(10, t)
    rest = n
    while rest:
        if rest % pow(10, t) != end:
            return False
        rest = rest // pow(10, t)
    return True