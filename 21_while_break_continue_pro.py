#Python program to print numbers from 0 to 10 using while, break and continue.
i = 0
while i <= 10:
    if(i == 6):
        i += 1
        continue
    if(i == 9):
        break
    print(i)
    i += 1
