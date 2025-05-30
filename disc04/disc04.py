def paths(m, n):
    """Return the number of paths from one corner of an
    M by N grid to the opposite corner.
    >>> paths(2, 2)
    2
    >>> paths(5, 7)
    210
    >>> paths(117, 1)
    1
    >>> paths(1, 157)
    1
    """
    ans = 0
    if m == 1 or n == 1:
        return 1
    ans += paths(m - 1, n) + paths(m, n - 1)
    return ans

def max_product(s):
    """Return the maximum product of non-consecutive elements of s.
    >>> max_product([10, 3, 1, 9, 2]) # 10 * 9
    90
    >>> max_product([5, 10, 5, 10, 5]) # 5 * 5 * 5
    125
    >>> max_product([]) # The product of no numbers is 1
    1
    """
    if len(s) == 0:
        return 1
    if len(s) == 1:
        return s[0]
    if len(s) == 2:
        return max(s[0], s[1])
    return max(s[0] * max_product(s[2:]), s[1] * max_product(s[3:]))

def sums(n, m):
    """Return lists that sum to n containing positive numbers up to m that
    have no adjacent repeats.
    >>> sums(5, 1)
    []
    >>> sums(5, 2)
    [[2, 1, 2]]
    >>> sums(5, 3)
    [[1, 3, 1], [2, 1, 2], [2, 3], [3, 2]]
    >>> sums(5, 5)
    [[1, 3, 1], [1, 4], [2, 1, 2], [2, 3], [3, 2], [4, 1], [5]]
    >>> sums(6, 3)
    [[1, 2, 1, 2], [1, 2, 3], [1, 3, 2], [2, 1, 2, 1], [2, 1, 3], [2, 3, 1], [3, 1, 2],
    [3, 2, 1]]
    """
    if n < 0:
        return []
    if n == 0:
        sums_to_zero = []
        # The only way to sum to zero using positives
        return [sums_to_zero] # Return a list of all the ways to sum to zero
    result = []
    for k in range(1, m + 1):
        result = result + [ [k] + rest for rest in sums(n - k, m) if rest == [] or rest[0] != k ]
    return result