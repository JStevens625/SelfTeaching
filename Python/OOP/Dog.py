class Dog(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def speak(self):
        print("Bark")
    
    def show(self):
        print(f"My name is {self.name} and I am {self.age} years old!")
    
    def set_age(self, age):
        self.age = age

tim = Dog("Tim",4)
bill = Dog("Bill",9)

tim.set_age(15)

tim.show()
bill.show()

