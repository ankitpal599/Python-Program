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