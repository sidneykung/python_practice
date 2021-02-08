# Write a function that takes two integers and prints out 
# the integers added together, 
# the difference between the two and 
# the integers multipled together 

int_1 = 5
int_2 = 20

def calc(int_1, int_2):
    add = int_1 + int_2
    sub = int_1 - int_2
    mult = int_1 * int_2
    return print(add, sub, mult)