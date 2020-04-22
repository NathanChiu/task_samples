
# Assuming n >= 0
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        # n = 2: 0 + 1 = 1
        # n = 3: 1 + 1 = 2
        # n = 4: 1 + 2 = 3
        return fib(n-1) + fib(n-2)

if __name__ == "__main__":
    print(fib(0))
    print(fib(1))
    print(fib(2))
    print(fib(3))
    print(fib(4))
    print(fib(5))
    print(fib(6))
    print(fib(7))
