#Python program to calculate factorial of a given number using functions.
def cal_fact(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    print(fact)
cal_fact(4)
cal_fact(6)    
