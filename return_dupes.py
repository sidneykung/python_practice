# write a function to return the duplicates of a list
# 02.01.2021

test_list = [1, 2, 3, 4, 4, 5, 6, 7, 7, 8, 9, 9]
# expected output is [4, 7, 9]


# solution

# empty list to record the duplicate numbers
# iterate through the list as a set
# if the number appears more than once
# append to extras

dupes = []
for x in set(test_list):
    if test_list.count(x) > 1:
        dupes.append(x)
print(dupes)
        
        
