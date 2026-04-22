# Storing objects in a dictionary

class Person:
    def __init__(self,name,gender,country):
        self.name = name
        self.gender = gender
        self.country = country

    # str function
    def __repr__(self):
        return f"name:{self.name},gender{self.gender},country:{self.country}"

# creating object
p1 = Person('mohit','male','india')
p2 = Person('elon','male','usa')

# storing objects inside a dictionary
peoples = {
    'p1':p1,
    'p2':p2
}

for i in peoples:
    print(peoples[i].name)