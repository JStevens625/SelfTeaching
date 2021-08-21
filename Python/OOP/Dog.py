class Dog(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def speak(self):
        print("Bark")
    
    def show(self):
        print(f"My name is {self.name} and I am {self.age} years old!")

tim = Dog("Tim",20)
print(d1.age)
print(d1.speak())