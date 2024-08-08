#!/usr/bin/python3
"""Contains a function"""

def find_peak(list_of_integers):
    """a function that finds a peak in a list of unsorted integers."""
    if len(list_of_integers) > 0:
        sorted_list = sorted(list_of_integers, reverse=True)
        
        return sorted_list[0]
    else:
        return "None"        
