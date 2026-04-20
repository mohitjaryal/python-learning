# reduce() is also a Higher-Order Function (HOF).
# reduce() applies a function cumulatively to the elements of an iterable and reduces it to a single value.

from functools import reduce

print(reduce(lambda x,y:x+y,[1,2,3,4,5,6]))