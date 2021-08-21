class Dog(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def speak(self):
        print("Bark")

d1 = Dog("Tim",20)
print(d1.age)
print(d1.speak())