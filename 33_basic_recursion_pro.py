#Python program to print numbers from 10 to 1 and calculate factorial of given number using recursion.
def num(n):
    if(n == 0):
        return
    print(n)
    num(n-1)
num(10)

def fact(n):
    if(n == 0 or n == 1):
        return 1
    else:
        return n * fact(n-1)
print(fact(6))
