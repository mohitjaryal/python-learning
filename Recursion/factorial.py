# Find factorial of a number (n!)

def factorial(n):
    if n == 0:
        return 1
    else:
        # factorial
        return n * factorial(n-1)

n = int(input('Enter a number :'))
print('Factorial is :',factorial(n))