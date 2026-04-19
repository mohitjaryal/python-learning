# it is a high order function
# it is used to apply a function to every item in an iterable (like a list, tuple, etc.) and return the results.

# list
L = [1, 2]
# this lambda function will do the square of the given input
print(list(map(lambda x: x**2, L)))