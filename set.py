# Write a Python program to create a set.
my_set = set()
print(my_set)


# Write a Python program to iteration over sets.
my_set = set('Mikael')
print(my_set)


# Write a Python program to add members(s) in a set.
my_set = {'Bob','John','Max'}
my_set.add('Mike')
print(my_set)


# Write a Python program to remove item(s) from set.
my_set = {11,'car',12,12,13,'bomb'}
my_set.remove('bomb')
print(my_set)


# Write a Python program to remove an item from a set
# if it is present in the set.
my_set = {'Mikael','Saribekyan',23}
my_set.discard(24)
print(my_set)


# Write a Python program to create an intersection of
# sets.
my_set = {'City','Country','River'}
new_set = {'human','car','City'}
my_set.intersection_update(new_set)
print(my_set)


# Write a Python program to create a union of sets.
set1 = {'a','b','c'}
set2 = {'d','e','f'}
set3 = set1.union(set2)
print(set3)



# Write a Python program to issubset and issuperset.
set4 = {'a','b','c','d'}
set5 = {'e','f','g','h','a','c','d','b'}
set6 = set4.issubset(set5)
print(set6)


set7 = {"f", "e", "d", "c", "b", "a","l","m","q"} 
set8 = {"a", "b", "c"}
set9 = set7.issuperset(set8) 
print(set9)


# Write a Python program to clear a set.
clear_set = {"Mika","Saribekyan","23","10",1995}
clear_set.clear()
print(clear_set)


# Write a Python program to find maximum and the
# minimum value in a set.
sets = set([1,2,3,4,5,9,10,11,25,35,45])
print(min(sets))


sets2 = set([1,2,3,4,5,9,10,11,25,35,45])
print(max(sets))


# Write a Python program to find the length of a set.
sets3= {'M','i','k','a'}
print(len(sets3))