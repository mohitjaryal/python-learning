"""
Reference Variables
Reference variables hold the objects
We can create objects without reference variable as well
An object can have multiple reference variables
Assigning a new reference variable to an existing object does not create a new object

"""

# object without a refrence
class Person:
    def __init__(self,name,country):
        self.name = name
        self.country = country

# here p is the refrence variable that holds the address of the Person class's object
p = Person()