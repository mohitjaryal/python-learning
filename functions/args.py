# *args
# it allows us to pass a variaable number of non keyword argument to a function

# this *args now will handle n number of inputs 
def multiply(*args):
    product = 1

    for i in args:
        product = product *i

    return product

print(multiply(2,3,4,5,3,2,90))