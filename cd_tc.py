"""Time complexity"""


""" Exercise 1"""

"""Categoize New Member"""
# To be a senior, a member must be at least 55 years old and have a handicap greater than 7. 
# In this croquet club, handicaps range from -2 to +26; the better the player the lower the handicap.

# Input
# Input will consist of a list of pairs. 
# Each pair contains information for a single potential member. 
# Information consists of an integer for the person's age and an integer for the person's handicap.

# Output
# Output will consist of a list of string values (in Haskell and C: Open or Senior) stating whether the respective member is to be placed in the senior or open category.

# Example
# input =  [[18, 20], [45, 2], [61, 12], [37, 6], [21, 21], [78, 9]]
# output = ["Open", "Open", "Senior", "Open", "Open", "Senior"]

def open_or_senior(data):
    open_list = []
    """ O(n)"""
    for i in range(len(data)):
        if data[i][0] < 55:
            open_list.append("Open")
        elif data[i][0] >= 55 and data[i][1] <= 7:
            open_list.append("Open")
        elif data[i][0] >= 55 and data[i][1] >= 7:
            open_list.append("Senior")

    return open_list

"""Exercise 2"""
""" NUMBER OF OCCURENCES"""
# sample = [0, 1, 2, 2, 3]
# number_of_occurrences(0, sample) == 1
# number_of_occurrences(4, sample) == 0
# number_of_occurrences(2, sample) == 2
# number_of_occurrences(3, sample) == 1


def number_of_occurrences(element, sample):
    """ O(n)"""
    for i in range(len(sample)):
        return sample.count(element)
    


"""Exercise 3"""
"""SUM MIXED ARRAY"""
# Given an array of integers as strings and numbers, return the sum of the array values as if all were numbers.
# Return your answer as a number.

def sum_mix(arr):
    """ O(1)"""
    a_list = [int(a_list) for a_list in arr]
    return sum(a_list)