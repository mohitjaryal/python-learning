# Inheritance
# We can access -> Constructor, Non private Attributes and Non Private methods


# user class (Parent class)
class User:
    def __init__(self, name):
        self.name = name

    def login(self):
        print('Login')

# Student class (Child class)
class Student(User):
    def enroll(self):
        print('Enrolled successfully')


u = User('Mohit')
s = Student('Mohit')

print(s.name)