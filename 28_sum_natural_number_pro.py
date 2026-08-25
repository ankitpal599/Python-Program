#Python program to find the sum of the first n natural numbers using while and for loop.
n = 6
sum = 0
i = 1
while i <= n:
    sum += i
    i += 1
print("total sum =", sum, ("\n"))
n = 8
sum = 0
for i in range(1, n + 1):
    sum += i
print("total sum =", sum)
