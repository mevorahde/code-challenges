# -*- coding: utf-8 -*-
"""
PDXPythonPirates/code-challenges: Warm Up Challenge: Sorting
sort_names.py
Created on Fri Nov  30
@author: David E. Mevorah
"""

# List of names, last name is out of order
names = ["Anna Smith", "John Anderson", "Cliff Bates", "Jimmy Garoppolo", "Jerry Rice", "James Garoppolo"]


# Function that sorts the names from the 'names' list by last name in alphabetical order.
def sort_by_last(names):
    # key is a set of instructions of what to sort by.
    # lambda is a single parameter, in this case 's', then the action, split by last name '[1]'
    # last action is sorting the 'names' list by the last name split.
    names.sort(key=lambda s: s.split()[1])
    print(names)


# Call the 'sort_by_last' function, using the 'names' list as it's argument.
sort_by_last(names)