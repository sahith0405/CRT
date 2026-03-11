# '''
# Arrays:
# 1. List ==> built-in Data Structure
#     1. Use [] to create a list
#     2. list is heterogeneous
#     3. list is mutable
#     4. List is indexed
#     5. List is ordered
#     6. List allows duplicate values

# 2. Array using array module
# 3. Array using numpy module
# '''
# li = [1, 12.5, True, "Chaitu", 7 + 9j]
# print(li, type(li))

# print(len(li))

# li[2] = False
# print(li)

# # add elements
# li.append(100)
# print(li)

# li.insert(3,"685158630")
# print(li)

# li.extend([1,23,45,6,7,])
# print(li)

# # remove elements
# li.pop()  # index in range 
# print(li)

# li.clear()
# print(li)

import array
arr = array.array('i', [1,2,3,4,5])

print("Hello")

