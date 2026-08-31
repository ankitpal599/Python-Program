#Python program to calculate the sum of the first n natural numbers using recursion.
def calc_sum(n):
    if(n == 0):
        return 0
    return calc_sum(n-1) + n
sum = calc_sum(15)
print(sum)
