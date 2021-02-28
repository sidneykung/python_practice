# Given a string s consists of some words separated by spaces, return the length of the last word in the string. 
# If the last word does not exist, return 0.

# example
# input: s = "Hello World"
# output: 5

def lengthOfLastWord(self, s: str) -> int:
    new_list = s.split()
    if len(new_list) >= 1:
        return len(new_list[-1])
    else:
        return 0