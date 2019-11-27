import pygame 
# dadsa
hi = "hello python"
print(3/2)
'''
This is a multiline
comment.
'''
num = 4.5
print(type(num))

# 4 types of data structure
# 1: Array/list
#  a collection which is ordered and changeable. Allows duplicate members.
thislist = ["apple", "banana", "cherry"]
print(thislist[2:5]) # get from index 2 to not including 5

# 2: tuple: 
# A tuple is a collection which is ordered and unchangeable. In Python tuples are written with round brackets.
thistuple = ("apple", "banana", "cherry")
print(thistuple[1])

# 3: set : https://www.w3schools.com/python/python_sets.asp 
# A set is a collection which is unordered and unindexed. In Python sets are written with curly brackets.
thisset = {"apple", "banana", "cherry"}
for x in thisset:
  print(x)
# Check if "banana" is present in the set:
print("banana" in thisset)
thisset.add("orange") # add item
thisset.update(["orange", "mango", "grapes"]) # Add multiple items to a set, using the update() method:
print(len(thisset)) # Get the Length of a Set
thisset.remove("banana") # remove item, remove() will raise an error if item doesn't exist
thisset.discard("banana") # use discard if not want to raise error
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2)

from testFold.test import printing, hey

printing()
hey()


# 4: dictionary 

