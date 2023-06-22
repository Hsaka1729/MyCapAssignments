# -*- coding: utf-8 -*-
"""
Created on Thu Jun 22 21:20:22 2023

@author: AKASH P.K
"""
#Creating lists
list1= [12,-7,5,64,-14]
list2 = [12,14,-95,3]
n=1
#Creating loop to print the positive numbers from the list1
for n in range(len(list1)):
#decision making
    if(list1[n]>0):
#diplaying the positive numbers        
     print(list1[n])
     n=n+1
#Creating loop to print the positive numbers from the list2
for i in range(len(list2)):
#decision making
    if(list2[i]>0):
#diplaying the positive numbers        
     print(list2[i])
     i=i+1