# recursion1.py
#   A collection of simple recursive functions
#   and their looping counterparts


def loopFact(n):
    # returns factorial of n
    fact=1
    for i in range(1,n+1):
        fact=fact*i
    return fact

def recFact(n):
    # returns factorial of n
    if n == 0:
        return 1
    else:
        return n * recFact(n-1)


def loopPower(a, n):
    # returns 'a' raised to int power 'n'
    ans = 1
    for i in range(n):
        ans = ans * a
    return ans

def recPower(a,n):
    # returns 'a' raised to int power 'n'
    if n == 0:
        return 1
    else:
        factor = recPower(a, n//2)
        if n % 2 == 0: # n is even
            return factor * factor
        else:
            return factor * factor * a


def loopFib(n):
    # returns the nth Fibonacci number
    curr = 1
    prev = 1
    for i in range(n-2):
        curr, prev = curr+prev, curr
    return curr

def recFib(n):
    # returns nth Fibonacci number
    # Note: this algorithm is exceedingly inefficient!
    if n < 3:
        return 1
    else:
        return recFib(n-1) + recFib(n-2)
