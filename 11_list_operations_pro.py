#Python program to perform various list operations.
evenlist = [2, 4, 6, 8, 10, 12, 14]
print(evenlist[1:4])
print(evenlist[-3:-1])

oddlist = [3, 1, 5, 9, 7, 11, 13]
oddlist.append(15)
print(oddlist)
print(oddlist.sort())
print(oddlist)
print(oddlist.sort(reverse=True))
print(oddlist)
oddlist.reverse()
print(oddlist)
oddlist.insert(2,15)
print(oddlist)
oddlist.remove(3)
print(oddlist)

