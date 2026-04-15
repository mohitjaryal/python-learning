# typles are immutable so if you want to add ,remove or change anything then first you must convert tuple into list 

# crating a tuple
countries = ('India','USA','Russia','Germany','France')
print('Before :',countries)

# converting tuple into list
temp = list(countries)

print(type(temp))

# adding australia to temp variable
temp.append('Australia')

# converting tem (list) into tuple
countries = tuple(temp)

print('After :',countries)

print(type(countries))