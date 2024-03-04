"""
    this is the homework of iteration
    In some problem, iteration might not be the best solution!
    ***YOU DONT HAVE TO FILL IN ALL BLANKS IF YOUR CODE IS GOOD ENOUGH***
"""

def gcd(m,n):
    """
    find the greatest common divisor between two numbers using iteration
    definition of gcd: gcd is the greatest number that can divide the two numbers

    hint: the builtin function min(m,n) returns the smaller one of the two numbers

    Sample output:
    >>> gcd(1,2)
    1
    >>> gcd(100,50)
    50
    >>> gcd(86,92)
    2
    >>> gcd(1001,70)
    7
    """
    assert m > 0 and n > 0; "only receive positive numbers"
    ________
    while _____:
        if _______:
            _________
        ________
    __________


def lcm(m,n):
    """
    find the least common multiplier between two numbers using iteration
    definition of lcm: lcm is the least number that can be divided by the two numbers

    hint: the builtin function max(m,n) returns the bigger one of the two numbers
    Sample output:
    >>> lcm(1,1)
    1
    >>> lcm(1,2)
    2
    >>> lcm(100,50)
    100
    >>> lcm(78,12)
    156
    >>> lcm(89,56)
    4984
    """
    assert m > 0 and n > 0; "only receive positive numbers"
    _________
    while _______:
        if ________:
            _________
        ________
    __________

def collatz(x):
    """
    find how many steps are needed to narrow down the number to 1 in a collatz conjecture using iteration

    >>> collatz(1)
    1
    >>> collatz(100)
    25
    """
    ________
    while _______:
        if _________:
            _________
        else:
            _________
        ________
    ________

def is_prime(x):
    """
    determine if a number is prime using iteration. A prime number can only be divided by 1 and itself
    >>> is_prime(2)
    True
    >>> is_prime(0)
    False
    >>> is_prime(103)
    False
    >>> is_prime(1001)
    True
    """
    assert x > 0, "only receive positive numbers"
    _______
    _______
    _______
    while ______:
        if _______:
            ________
        ________
    __________
    
    
def get_digit(x):
    """return how many digits in a number """
    if abs(x) == 0:
        return 0
    else:
        return get_digit(x//10) + 1

def all_prime(x):
    """
    only keep prime digits. 

    hint: use the is_prime() function and get_digit() function
    use pow() function -> pow(2,10) == 2^10

    >>> all_prime(666)
    0
    >>> all_prime(101300)
    113
    >>> all_prime(9257708662)
    25772
    >>> all_prime(9256851230)
    255123
    """
    ________
    while _______:
        __________
        if __________:
            ___________
        _________
    _________