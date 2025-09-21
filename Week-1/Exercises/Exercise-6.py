"""
Write a script that lists all the prime numbers between 1 and 10000.
(A prime number is an integer greater or equal to 2 which has no divisors except 1 and itself). 
Hint: Write an is_factor helper function.
"""

def is_factor(d, n):
    """True iff (if and only if) d is a divisor of n."""
    return n%d==0
    pass

def is_prime(n):
    for d in range(2,n):
        if is_factor(d,n):
            return
    return n 
    pass

list_of_primes = [is_prime(i) for i in range(1,10) if is_prime(i)!=None]
print(list_of_primes)