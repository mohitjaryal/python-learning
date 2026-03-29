# 1. Positional arguments
def greet(name, age):
    print("Hello", name, "you are", age, "years old")

greet("Alice", 25)

# 2. Default arguments
def greet_default(name, age=18):
    print("Hello", name, "you are", age, "years old")

greet_default("Bob")
greet_default("Charlie", 30)

# 3. Keyword arguments
def greet_keyword(name, age):
    print("Hello", name, "you are", age, "years old")

greet_keyword(age=22, name="David")

# 4. Variable-length arguments (*args)
def add_numbers(*args):
    total = 0
    for num in args:
        total += num
    print("Sum:", total)

add_numbers(1, 2, 3)
add_numbers(5, 10, 15, 20)

# 5. Variable-length keyword arguments (**kwargs)
def student_info(**kwargs):
    for key, value in kwargs.items():
        print(key, ":", value)

student_info(name="Emma", age=20, course="Python")
student_info(name="Frank", city="Delhi")