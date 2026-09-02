#Python program to print Fibonacci series.
n = int(input("enter the number term:"))
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)
for i in range (n):
    print(fibonacci(i), end="")
