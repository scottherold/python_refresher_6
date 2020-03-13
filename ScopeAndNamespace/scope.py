# Python allows for functions to nested with functions
# A common use for this is initializer functions (and recursion)


# factorial function with iteration
def fact(n):
    """ calculate n! iteratively """
    result = 1
    # factorial calculation
    if n > 1:
        for f in range(2, n + 1):
            result *= f
    return result


# factorial with recursion (more efficient)
def factorial(n):
    # n! can also be defined as n * (n - 1)!
    """ calculates n! recursively """
    if n <= 1:
        return 1
    else:
        return n * factorial(n-1)


# fib sequence with recursion
def fib(n):
    """ F(n) = F(n - 1) + F(n - 2) """
    if n <2:
        return n
    else:
        return fib(n-1) + fib(n-2)


# fib sequence, alternative with iteration (more efficient)
def fibonacci(n):
    if n == 0:
        result = 0
    elif n == 1:
        result = 1
    else: 
        n_minus1 = 1
        n_minus2 = 0
        for f in range(1, n):
            result = n_minus2 + n_minus1
            n_minus2 = n_minus1
            n_minus1 = result
    return result

for i in range(36):
    print(i, fibonacci(i))