# -*- coding: utf-8 -*-
"""
Created on Mon Oct  4 15:52:10 2021

@author: Nikhil J
@email : se.nikhilj45@gmail.com
"""

# >>>>>>>>>> Numpy <<<<<<<<<<<<<

# >>>>>>>> SECTION 1 : INTRODUCTION

# It creates an N Dimensional Array 

import numpy as np

a1 = np.array([1,2,3,4,5,6]) # create an array default dtype for numeric value is int32

# the datatype can also be specified
# create an array matrix 2 x 3 , specified dtype : int64

a2 = np.array([[1,2,3],[4,5,6]], np.int64)
print(" a1 and a2 are called ndarrays")

# Create a random array of size (3,2) with values ranging 0,1,2,3,4
# range doesnt include the max value specified
a3 = np.random.randint(0,5,(3,2))

# >>>> Reshaping the arrays

# to find the shape of array 
print('The Shape of array is' + str(a3.shape))

# to reshape them

print(a3.reshape(1,6)) # convert array of length 1
print(a3.reshape(2,3)) # convert to a matrix of 2 X 3 or an array of length 2
print(a3.transpose())  # Transpose an array dimension # interchange rows and columns

# >>>>>>> Indexing , Slicing
# provide the index length/ row wise index = range(0,len(a2.shape))

print(len(a2.shape)) # returns 2 so rows have index 0,1
print(a2[0,:])       # return : all the elements in first row index 0
print(a2[0,1])       # return : element in first row and second column

# lets mutate the value 2 to 7 in first row and second column

a2[0,1] =7

print(a2) # They are mutable

a2[0,:] = [10, 9,8]
print(a2) # We have changed the values of first rows

# >>>>>>>>>> Arithematic Operations : ELEMENTWISE

a2 + a3  # Not of same dimension cannot add . Proof that array Follow Matrix Algebra

a2 + a3.transpose() # Now a3 was reshaped in shape of 2 they supported addition
a2.reshape(3,2) + a3 # Vice Versa is Also " TRUE "

# Generating Random Sample Data
# RANDOM INT
# use numpy.random.randomint(low, high, (shape))
# it generates random sample everytime running this code
random_1 = np.random.randint(0,5,(2,2))

# RANDOM SEED >>>>>>>>> np.random.seed(number) any arbitrary number
# These values are random but they dont change for multiple running this code
np.random.seed(123)
random_2 = np.random.randint(0,11,(4,4))

# RANDOM CHOICE >>>> numpy.random.choice(array,number,replace)
# array : existing or newly defined complete or a slice
# number : number of elements of which sample is to be formed
# replace : bool : Repeatition of elements allowed or not in sample

# This can be an array or slice of an array
# Still it will generate a random sample

print(np.random.choice(random_2[0,:],4,replace = True)) # repeatition allowed so multiple same values
print(np.random.choice(random_2[0,:],4,replace = False)) # all values are different


#__ ___ ___ ___ ____ ____ ____ ____ _____ _____ _____ _____ ___
# >>>>>>>>>> SECTION 2 : ARRAY CONSTRUCTION <<<<<<<<<<<<<< #   |
#___ ____ ____ ____ ____ ____ ____ _____ ____ _____ _____ _____|        

# There are two ways
# 1. Array Creation Routines 2. ndarray

# NDARRAY : numpy.ndarray(shape, dtype=float, buffer=None, offset=0, strides=None, order=None)

ar=np.ndarray(shape =(2,1), dtype=int)
a = np.array([1,2,3.9])
a.astype(int) # 3.9 got auto-truncated to 3 while changing datatype 
b = np.ones((2,2)).astype(int)
x = np.append( arr = np.ones((2,2)).astype(int),values= random_1,axis =1)
