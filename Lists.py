# -*- coding: utf-8 -*-
"""
Created on Fri Sep  3 21:49:19 2021

@author: Nikhil
"""
# Python Lists : Creation Methods Operation Comprehension Iteration
list1 = []  # creates an empty list
list1
list2 = [10, 20, 30, 40, 50]  # Unidimensional List
list2 
list3 = ['Nikhil', 'Devishi', 'Vinayak', 'Kirti', 'Spandan', 'Vashishti']  # List of Strings
list4 = [['Walker', 'White', 'Singature'], 10, True, 'Fortuner',10]  # Heterogeneous nature of list and can hold multiple same values
# Indexing Slicing and Concatenation #
print(list2[0])  # Will print the first number in list # index = len(list) -1
print(list3[0:3])  # printing indexes 0 1 2 except 3. First three values are
list8 = str(list2[0]) + str(list3[0:3] ) # cancatenator "+" to update empty list1 *** Mutation possible ****
list5 = list1 + list2  # combining list1 and list2

# Append Extend Insert
# Append adds a value at the end of list : Only one value can be added each time : for multiple use iteration
list2.append(4)  # value 4 will appear at the end of list2
print(list2)
list2.remove(4)  # value 4 will be removed from list2
print(list2)
# Multiple appending 
for i in range(1,4):
    list2.append(i)
    i = i + 1
    print(list2)

