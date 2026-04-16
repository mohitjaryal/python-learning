# symmetric difference -> this gives all the values that are not common in both sets

s1 = {1,2,3,6}
s2 = {4,5,6,2}

# storing result
result = s1.symmetric_difference(s2)

# printing the result
print('Intersection :',result)
