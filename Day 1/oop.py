#LEARNING OOP

#CREATING A SIMPLE CLASS IN PYTHON

class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        return f"{self.name} says hello!"
    
dog = Animal("charlie")
print(dog.speak())

#CREATING A SUBCLASS OR SO CALLED INHERITANCE
print("---------------------INHERITANCE-------------------------------")

class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} says Hello! "
    
class Dog(Animal):
    def speak(self):
        return f"{self.name} Barks!"
    
dog = Dog("Shiwam")
print(dog.speak())

# USING THE SUPER() FUNCTION
print("--------------------SUPER() FUNCTION------------------------")

class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        return f"{self.name} says hello! "
    
class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed
    
dog = Dog("shiwam", "human")
print(dog.name)
print(dog.breed)