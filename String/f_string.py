# f string is used in string formatting

# old method
# letter = 'Hi my name is {1}  and I am from {2}'

country ='India'
name = 'Mohit'

# using f string
print(f'Hi my name is {name} and I am from {country}')

# we can use .2f -> it will only take 2 decimal places
# e.g

price = 98.0989
print(f'Price is only {price:.2f}')