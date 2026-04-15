# recursion is the process of defining something in terms of itself

def factorial(n):
    if n ==0:
        return 1
    else:
        # function calling inside itself
        return n * factorial(n-1)
n = 5
print('Number :', n)
print('Factorial :', factorial(n))    