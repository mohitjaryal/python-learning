# this only prints the items that are present in the original set and not in both the sets

cities ={'Mumbai','Banglore','Delhi','Pune'} 
cities2 = {'CA','LA','NY','Delhi','Pune'}
cities3 = cities.difference(cities2)
print(cities3) 