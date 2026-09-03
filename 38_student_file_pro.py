name = input("enter student name:")
roll = input("enter roll number:")
cgpa = input("enter cgpa:")
with open("student.txt","w")as file:
    file.write("Name:Ankit Pal\n")
    file.write("Roll Number:25CSE30\n")
    file.write("CGPA:7.2\n")
print("student information saved.")