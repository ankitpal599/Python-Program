#Python program to check whether given list is a palindrome or not a palindrome.
list1 = [1,2,3,4,3,2,1]
copy_list1 = list1.copy()
copy_list1.reverse()
if(copy_list1 == list1):
    print("palindrome")
else:
    print("NOT a palindrome")
    
list2 = [1,3,2,5,4,7,6]
copy_list2 = list2.copy()
copy_list2.reverse()
if(copy_list2 == list2):
    print("palindrome")
else:
    print("NOT a palindrome")
