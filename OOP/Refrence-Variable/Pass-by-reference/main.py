# Pass by reference

class Person:
    def __init__(self,name,gender):
        self.name = name
        self.gender = gender


# greet function
def greet(person):
    print('Hi i am',person.name, 'and i am a',person.gender)


p = Person('Mohit','Boy')

# passing object of the class as a input to a function
greet(p)

# objects of the user defined classes are mutable just like lists,sets and dictionary