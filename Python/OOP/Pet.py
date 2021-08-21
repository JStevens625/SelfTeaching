class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def show(self):
        print(f"My name is {self.name} and I am {self.age} years old!")

    def set_age(self, age):
        self.age = age

class Dog(Pet):
    
    def speak(self):
        print("Bark")
        
tim = Dog("Tim",4)
bill = Dog("Bill",9)

tim.set_age(15)

tim.show()
bill.show()

