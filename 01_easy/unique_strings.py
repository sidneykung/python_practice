# Write a program to determine if a string contains only unique characters. Return true if it does and false otherwise.
# https://www.codewars.com/kata/553e8b195b853c6db4000048/train/python

# The string may contain any of the 128 ASCII characters. Characters are case-sensitive, e.g. 'a' and 'A' are considered different characters.

# technique: run 2 loops with variable i and j. 
# compare str[i] and str[j]. 
# if they become equal at any point, return false. 

def has_unique_chars(str):
    # if at any time we encounter 2 same characters, return false
    for i in range(len(str)):
        for j in range(i + 1,len(str)): 
            if(str[i] == str[j]):
                return False;
    # if no duplicate characters encountered, return true
    return True;
 
# time complexity: (O(n2))