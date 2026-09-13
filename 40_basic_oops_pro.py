#Python program to create a student class, initialize the student's name, age and marks using a constructor and display the student's details.
class Student:
    def __init__(self, name, age, marks):
        self.name = name
        self.age = age
        self.marks = marks

    def display(self):
     print("Name:",self.name)
     print("Age:",self.age)
     print("Marks:",self.marks)

student1 = Student("Ankit", 19, 85)
student1.display()
