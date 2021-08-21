class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def show(self):
        print(f"My name is {self.name} and I am {self.age} years old, and I am a {type(self).__name__}")

    def set_age(self, age):
        self.age = age
    
    def speak(self):
        print("What am I?")

class Dog(Pet):
    dogs = []

    def __init__(self, name, age):
        super().__init__(name, age)
        self.dogs.append(self)

    @staticmethod
    def speak(n):
        for _ in range(n):
            print("Bork")
    
    @classmethod
    def num_dogs(cls):
        return len(cls.dogs)

class Cat(Pet):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color
    
    @staticmethod
    def speak(n):
        for _ in range(n):
            print("Meow")
    
    

tim = Cat("Tim",4, "Calico")
bill = Dog("Bill",9)

tim.set_age(15)

tim.show()
bill.show()
tim.speak(3)

print(Dog.num_dogs())