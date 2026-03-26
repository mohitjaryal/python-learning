# Match case statement in python

x = 4

# we are now matching variable x
match x:

    case 0:
        print(x,'is 0')
    case 4:
        print(x,'is 4')
    case _:
        print(x)