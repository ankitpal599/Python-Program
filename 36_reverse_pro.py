#Python program to print the reverse digits of a given number.
num = int(input("enter a number:"))
def reverse_number(n):
    rev = 0
    while n > 0:
        digit = n % 10
        rev = rev * 10 + digit
        n = n//10
    return rev
print("reverse =",reverse_number(num))
