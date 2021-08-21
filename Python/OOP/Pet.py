class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def show(self):
        print(f"My name is {self.name} and I am {self.age} years old!")

    def set_age(self, age):
        self.age = age
    
    def speak(self):
        print("What am I?")

class Dog(Pet):
    
    def speak(self):
        print("Bork Bork!")

class Cat(Pet):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color
    
    def speak(self):
        print("Meow Meow!")
    
    

tim = Cat("Tim",4, "Calico")
bill = Dog("Bill",9)

tim.set_age(15)

tim.show()
bill.show()
tim.speak()
