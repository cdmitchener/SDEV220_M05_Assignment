# Square
my_list = [5, 4, 3]

# Map over new_list and square each number in  my_list
new_list = list(map(lambda num: num**2, my_list))
print(new_list)

# List Sorting
a = [(0,2), (4,3), (10,-1), (9,9)]

# Sort by first key
# a.sort()
# print(a)

# Sort by second key (default parameter is lambda of x where x each item, or tuple, and use the second value which is what will return)
a.sort(key=lambda x: x[1])
print(a)