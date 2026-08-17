#Python program to calculate area and perimeter of square and rectangle by taking input from the user.
side = int(input("enter square side:"))
#we can use float instead of int for decimal number.
print("area=",side*side)
print("perimeter=",4*side,"\n")
length = int(input("enter length:"))
breadth = int(input("enter breadth:"))
#we can use float instead of int if any of the both no. are decimal number.
print("area=",length*breadth)
print("perimeter=",2*length+breadth)
