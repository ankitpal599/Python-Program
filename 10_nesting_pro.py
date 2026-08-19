#Python program to check age eligibilty for IAS exam using nested if-else statements.
age = int(input("enter the age:"))
if(age >= 18):
    if(age > 35):
        print("not eligible for IAS exam")
    else:
        print("eligible for IAS exam" )
else:
    print("not eligible for IAS exam")
