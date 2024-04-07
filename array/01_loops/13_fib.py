"""
fib(n) - returns the nth Fibonacci number
Example:
fib(1) -> 1
fib(2) -> 1
fib(3) -> 2
fib(4) -> 3
fib(5) -> 5
fib(6) -> 8
fib(7) -> 13
fib(8) -> 21
fib(9) -> 34
fib(10) -> 55
"""

import time
from functools import lru_cache

def fib_iter(n):
    # Iterative
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    
    return a

@lru_cache
def fib_rec(n):
    # Recursion
    if n <= 1:
        return n
    return fib_rec(n-1) + fib_rec(n-2) 


def fib_memo(n, memo={}):
    # Dynamic Programming memoization - top down
    if n <= 1:
        return n
    if n in memo:
        return memo[n]
    memo[n] = fib_memo(n-1, memo) + fib_memo(n-2, memo)
    return memo[n]


def fib_tabluation(n):
    # Dynamic Programming tabulation - bottom up
    ans = [0, 1]
    for i in range(2, n+1):
        num = ans[i-1] + ans[i-2]
        ans.append(num)
    return ans[n]


if __name__ == "__main__": 
    n = 100
    start_time = time.time()
    print(fib_iter(n))
    end_time = time.time()
    print("fib_iter execution time:", end_time - start_time)

    start_time = time.time()
    print(fib_rec(n))
    end_time = time.time()
    print("fib_rec execution time:", end_time - start_time)

    start_time = time.time()
    print(fib_memo(n))
    end_time = time.time()
    print("fib_memo execution time:", end_time - start_time)

    start_time = time.time()
    print(fib_tabluation(n))
    end_time = time.time()
    print("fib_tabluation execution time:", end_time - start_time)