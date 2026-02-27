#Animal Shelter system.

class Animal:
    def __init__(self, name, age, weight, species):
        self.name = name
        self.age = age
        self.weight = weight
        self.species = species

#return a friendly description of the animal
    def __str__(self):
        return f"{self.name} | Age: {self.age} | Species: {self.species} | Weight: {self.weight}kg"

#return the animal's age
    def __len__(self):
        return self.age
    
# compare two animals as equal if they have the same name and species
#remember to use isinstance, that is where you were wrong.
   def __eq__(self, other):
    if isinstance(other, Animal):
        if self.name == other.name and self.species == other.species:
            return True
    return False


#Polymorphism in child classes. super().__init__() is how you hand that data up
class Dog(Animal):
    def __init__(self, name, age, weight, breed):
        super().__init__(name, age, weight, species="Dog")  # call Animal's __init__
        self.breed = breed

    def __str__(self):
        return f"{self.name} | Age: {self.age} | Breed: {self.breed}"

    def makesound(self): #polymorphism
        print(f"The {self.name} sound is : Woof!")

class Cat(Animal):
    def __init__(self, name, age, weight, breed):
        super().__init__(name, age, weight, species="Cat")  # call Animal's __init__
        self.breed = breed

    def __str__(self):
        return f"{self.name} | Age: {self.age} | Breed: {self.breed}"

    def makesound(self):
        print(f"The {self.name} sound is : Meow!")

class Bird(Animal): #inherits from Animal
    def __init__(self, name, age, weight, can_fly):
        super().__init__(name, age, weight, species="Dog")  # call Animal's __init__
        self.can_fly = can_fly

    def __str__(self):
        return f"{self.name} | Age: {self.age} | Breed: {self.breed}"

    def makesound(self):
        print(f"The {self.name} sound is : kaka!")

    

dog1 = Dog("Rex", age=3, weight=20, breed="Labrador")
cat1 = Cat("Mimi", age=2, weight=4, breed="Persian")
bird1 = Bird("Tweety", age=1, weight=0.5, can_fly=True)
