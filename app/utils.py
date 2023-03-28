def fib(n):
    if n <= 1:
        return n
    else:
        print(f"Calculating fib({n - 1}) + fib({n - 2})")
        return fib(n - 1) + fib(n - 2)