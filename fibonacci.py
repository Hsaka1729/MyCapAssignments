# -*- coding: utf-8 -*-
"""
Created on Thu Jun 22 22:35:37 2023

@author: AKASH P.K
"""
def fibonacci(n):
    a, b = 0, 1

    print(a)
    if n > 1:
        print(b)

        for _ in range(2, n):
            a, b = b, a + b
            print(b)


# Test the function
num_terms = int(input("Enter the number of Fibonacci terms to generate: "))
fibonacci(num_terms)