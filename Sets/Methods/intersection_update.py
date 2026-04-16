# inersection update method
# this adds the values that are present in both the set

s1 = {1,2,3,6}
s2 = {4,5,6,2}

# intersection_update -> this will add all the common value present in s1 and s2 in s1
result = s1.intersection_update(s2)

# printing the result
print('Intersection update :',result)

print('s1 :',s1)
print('s2 :',s2)