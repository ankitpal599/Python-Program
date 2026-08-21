cities = {"Ayodhya", "Mathura", "Agra", "Ayodhya", "Lucknow", "Agra", "Mathura", "Delhi",  }
print(cities)
print(type(cities))
print(len(cities),"\n")
cities.add("Varanasi")
print(cities)
cities.remove("Agra")
print(cities)
cities.pop()
print(cities)
cities.clear()
print(cities)
#specialcase
set1 = {1, 2, 3, 5,}
set2 = {2, 4, 5, 6,}
print(set1.union(set2))
print(set1.intersection(set2))