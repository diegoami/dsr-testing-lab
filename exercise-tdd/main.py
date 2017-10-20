import unittest

# Returns the nth Fibonacci number
def fib(n):
    if n < 0:
        raise ValueError("arg must be > 0")
    elif n == 0:
        return 0
    else:
        fib_list = [1, 1]
        while n > len(fib_list):
            ft = fib_list[-1] + fib_list[-2]
            fib_list.append(ft)
        return fib_list[-1]



