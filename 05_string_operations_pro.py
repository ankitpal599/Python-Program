#Python program to perform various string operations.
Name = input("enter your  name:")
print("length of your name is", len(Name),"\n")
str = "I am currently pursuing BE fron CSE"
print(str.endswith("SE"))
print(str.endswith("am"))
str = "i belong to Ayodhya"
print(str.capitalize())
str = "I am currently living in Delhi"
print(str.replace("Delhi","Agra"))
str = "I am currently in first year"
print(str.find("currently"))
str = "I am learning Python and preparing for DSA"
print(str.count("a"))
