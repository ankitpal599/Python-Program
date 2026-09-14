 #Python program to demonstrate inheritance and polymorphism using an Animal class and its derived classes where each classs should have a speak() method that diplays the sound made by that animal.
class Animal:
    def speak(self):
        print("Animal makes a sound")
class Dog(Animal):
    def speak(self):
        print("Dog barks.")
class Cat(Animal):
    def speak(self):
        print("Cat meows.")
class Lion(Animal):
    def speak(self):
        print("Lion roars.")
dog1 = Dog()
dog1.speak()
cat1 = Cat()
cat1.speak()
lion1 = Lion()
lion1.speak()
