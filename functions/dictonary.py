# dictionaries parameters

def name(**names):
    print('Hello', names['fname'], names['mname'],names['lname'])


name(fname='Raja', mname='Ram', lname='Singh')