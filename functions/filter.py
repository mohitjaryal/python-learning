# filter() function
# It is a Higher-Order Function (HOF)
# A HOF is a function that:
# - takes another function as an argument, or
# - returns a function
# filter() applies a condition to each element of an iterable
# and returns an iterator of elements that satisfy the condition


# list
L = [1,23,5,7,4,64,34,2,4,7,8,9,10]
# filter() takes a function and an iterable 
print(list(filter(lambda x:x>5,L)))