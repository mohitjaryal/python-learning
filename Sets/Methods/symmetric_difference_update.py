# symmetric difference -> this gives all the values that are not common in both sets
 # all the uncommon values of s2 that are not present in s1 will be added to s1

s1 = {1, 2, 3, 6}
s2 = {4, 5, 6, 2}

# updating s1
s1.symmetric_difference_update(s2)

# printing updated s1
print('Symmetric Difference:', s1)