# Inheritance example

# Parent class 
class Phone:
    def __init__(self,price, brand, camera):
        print('Inside Parent constructor')
        self.__price = price
        self.brand = brand
        self.camera = camera

# If child class dosen't have any constructor then automatically Parent's class constructor is called 
# And if child class have a constructor then Parent's class constructor will never call 

# Child class
class SmartPhone(Phone):
    # constructor
    def __init__(self,os,ram):
        self.os = os
        self.ram = ram
        print('Inside Child class')

# object
s = SmartPhone('Apple',12)
