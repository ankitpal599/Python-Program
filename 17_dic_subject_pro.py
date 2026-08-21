#Python program to create an empty dictionary and to enter marks of 3 subjects from the user & store them in a dicitionary.
marks = {}
x = int(input("enter physics :"))
marks.update({"physics": x})
y = int(input("enter chemistry :"))
marks.update({"chemistry": y})
z = int(input("enter maths :"))
marks.update({"maths": z})
print(marks)
