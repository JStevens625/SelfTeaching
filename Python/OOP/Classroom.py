#!/usr/bin/python3

class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade
    
    def get_grade(self):
        return self.grade

class Course:
    def __init__(self, name, max_students):
        self.name = name
        self.max_students = max_students
        self.students = []
    
    def add_student(self, student):
        if len(self.students) < self.max_students:
            self.students.append(student)
            return True
        return False

    def get_average_grade(self):
        value = 0
        for student in self.students:
            value += student.get_grade()
        
        return value / len(self.students)


student1 = Student("Tim", 18, 70)
student2 = Student("Bill", 18, 90)
student3 = Student("Jill", 19, 97)

course = Course("Calculus", 2)
course.add_student(student1)
course.add_student(student2)
print(course.add_student(student3)) #Returns false because it was unable to add

print(course.get_average_grade())