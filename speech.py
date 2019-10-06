#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 04:55:07 2019

@author: tejas
"""


import numpy as np
from numpy.linalg import matrix_rank
print("-------Question 1-------")

def calc_freq(l):
    freq = {}
    for i in l:
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1
    return freq

arr = [1,1,2,1,3,2,6,5,2,3,3,3,4,4,4,4]
freq1 = calc_freq(arr)
for i in freq1:
    print("\nFrequency of ",str(i)+" is: "+str(freq1[i]))

print("\n-------Question 2-------\n")

arr = [0,0,0,1,1,1]
print("Input: ",arr)
count = 0
i = 0
while(count < len(arr)):
    if arr[i] == 0:
        arr = arr[:i]+arr[i+1:]
        arr.append(0)
    else:
        arr = arr[:i]+arr[i+1:]
        arr[:0] = [1]
        i += 1
    count += 1

print("Output: ",arr)

print("\n-------Question 3-------\n")

string = "this is a solution of the assignment"
print("Initial String: ",string," Length:",len(string))
n = int(np.random.random(1)*len(string))
string = string[:n]+string[n+1:]
print("Final String  : ",string," Length:",len(string))

print("\n-------Question 4-------\n")

z = np.ones((3,3))
print("Initial:\n\n",z,"\n")
z = np.pad(z,pad_width=1,mode="constant",constant_values=0)
print("Final:\n\n",z)

print("\n-------Question 5-------\n")

Z1 = np.random.randint(0,10,10)
Z2 = np.random.randint(0,10,10)
Z3 = np.intersect1d(Z1,Z2)
print("Array 1: ",Z1)
print("Array 2: ",Z2,"\n")
for i in Z1:
    if i in Z3:
        print("True",end=" ")
    else:
        print("False",end=" ")

print("\n\n-------Question 6-------\n")

Z1 = np.random.randint(0,10,10)
Z2 = np.random.randint(0,10,10)
Z3 = np.intersect1d(Z1,Z2)
print("Array 1: ",Z1,"\nArray 2: ",Z2,"\n\n")
print("Unique Elements: ",end=" ")
for i in Z1:
    if i not in Z3:
        print(i,end=" ")

for i in Z2:
    if i not in Z3:
        print(i,end=" ")
    
print("\n\n-------Question 7-------\n")

z1 = np.array((1,2,3,4,5))
z2 = np.array((6,7,8,9,0))
z3 = np.column_stack((z1,z2))
print(z3)

print("\n-------Question 8-------\n")

z = np.arange(9).reshape(3,3)
print("Matrix: \n",z,"\n\n")
print("Rank of the Matrix: ",matrix_rank(z),"\n\n")
print("Trace of the Matrix: ",np.trace(z),"\n\n")
//not able to pull request
print("Determinant of the Matrix: ",np.linalg.det(z),"\n\n")
//doing just for learning git
//it also give me free tshirt
