#Python program to find largest of the three numbers given bt the user.
num1 = int(input("enter first number:"))
num2 = int(input("ener second number:"))
num3 = int(input("enter third number:"))
if(num1 >= num2 and num1 >= num3):
    print("first number is largest",num1)
elif(num2 >= num3):
    print("second number is largest",num2)
else:
    print("third number is largest",num3)
