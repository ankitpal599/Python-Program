#Python program to print odd and even numbers from 1-20 using while loop.
i = 1
while i <= 20:
    if(i%2 == 0):
        i += 1
        continue
    print(i)
    i += 1
i = 1
while i <= 20:
    if(i%2 != 0):
        i += 1
        continue
    print(i)
    i += 1
