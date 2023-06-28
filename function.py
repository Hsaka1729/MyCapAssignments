# -*- coding: utf-8 -*-
"""
Created on Tue Jun 27 22:24:18 2023

@author: AKASH P.K
"""

def most_frequent(string):
    # Create an empty dictionary to store letter frequencies
    frequency = {}

    # Iterate through each character in the string
    for char in string:
        # Ignore non-alphabetic characters
        if char.isalpha():
            # Convert the character to lowercase for case-insensitive counting
            char = char.lower()
            # Update the frequency count for the character
            frequency[char] = frequency.get(char, 0) + 1

    # Sort the dictionary by values in descending order
    sorted_frequency = sorted(frequency.items(), key=lambda x: x[1], reverse=True)

    # Print the letters and their frequencies
    for char, count in sorted_frequency:
        print(char, "=", str(count).zfill(2))


# Test the function
input_string = input("Please enter a string: ")
most_frequent(input_string)
