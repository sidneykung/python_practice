https://leetcode.com/problems/reverse-integer/

# Given a signed 32-bit integer x, return x with its digits reversed. 
# If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

# example:
# input: x = 123
# output: 321

def reverse(self, x: int) -> int:
    stringed = str(abs(x))
    reversed_int = int(stringed[::-1])
    if reversed_int >=2**31 or reversed_int <= (2**31)*-1:
        return 0
    elif x < 0:
        return reversed_int * -1
    else:
        return reversed_int