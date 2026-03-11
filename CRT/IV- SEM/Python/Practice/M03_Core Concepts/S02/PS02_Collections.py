'''SET:
1.use {} to create a set
2.duplicate values are not allowed
3.unordered collection of items
4.mutable and undindexed
5.heterogeneous items are allowed
'''
# s = {True,12.45,10,1,9+5j}
# print(s,type(s))
#Add and Update Set:
A = {1,2,3,4,5}
B = {4,5,6,7,8}
A.add(6)
B.update({9,10})
print(A)
print(B)
#Remove and pop Set:
A.remove(6)# if the element is not present in the set it will throw an error
B.pop()# it will remove a random element from the set and return it
A.discard(7)# if the element is not present in the set it will not throw an error
print(A)
print(B)
A.clear()# it will remove all the elements from the set
print(A)
#difference and symmetric,union and intersection of sets:
A = {1,2,3,4,5}
B = {4,5,6,7,8}
print(A.difference(B))# it will return the elements that are present in A but not in B
print(B.difference(A))# it will return the elements that are present in B but not in A
print(A.symmetric_difference(B))# it will return the elements that are present in A or B but not in both
print(A.union(B))# it will return the elements that are present in A or B or both
print(A.intersection(B))# it will return the elements that are present in both A and B
#dictionary:
# it is a collection of key-value pairs
# it is mutable and unordered
# it is denoted by {}
# it is indexed by keys
# it is heterogeneous
d = {'name':'John','age':30,'city':'New York'}
print(d,type(d))
#Add and Update Dictionary:
d['country'] = 'USA'
d.update({'state':'NY'})
print(d)
#Remove and pop Dictionary:
d.pop('age')# it will remove the key-value pair with the specified key and return
d.popitem()# it will remove the last key-value pair and return it
print(d)
d.clear()# it will remove all the key-value pairs from the dictionary
print(d)