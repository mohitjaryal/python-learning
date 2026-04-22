# Collection of objects

# list of objects
class Person:
    def __init__(self,name,gender):
        self.name = name
        self.gender = gender

# objects
p1 = Person('mohit','male')
p2 = Person('rohit','male')
p3 = Person('priya','female')

# putting objects p1,p2,p3 in a list
L = [p1,p2,p3]

for i in L:
    print(i.name,i.gender)