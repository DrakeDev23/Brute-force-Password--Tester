import time
import random
from abc import ABC, abstractmethod

class Person(ABC):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @abstractmethod
    def Information(self):
        pass

class Student(Person):
    def __init__(self, name, age, position, ID):
        super().__init__(name, age)
        self.position = position
        self.ID = ID

    def Information(self):
        return f"Name: {self.name}\nAge: {self.age}\nPosition: {self.position}\nID: {self.ID}"

class Inputs:
    def GetData(self):
        name = input("Enter your name: ")
        age = int(input("Enter your age: "))
        position = input("Enter your position: ")
        ID = int(input("Enter your ID: "))

        return Student(name, age, position, ID)

class ShowInfo(Inputs):
    def Show(self):
        s = self.GetData()

        print(s.Information())


    
    