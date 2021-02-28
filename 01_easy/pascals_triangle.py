https://leetcode.com/problems/pascals-triangle/

# Given an integer numRows, return the first numRows of Pascal's triangle.

# In Pascal's triangle, each number is the sum of the two numbers directly above it.

# example
# input: numRows = 5
# output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]

class Solution(object):
    def generate(self, numRows):
        # instantiate list
        return_list = []
        prev_list = []
        # iterating through rows
        for index in range (0,numRows):
            # if first list
            if index == 0: 
                cur_list = [1]
            # if note first list
            else:
                # always start wtih 1
                cur_list = [1]
                # add between 1's to get inner items
                for count in range((len(prev_list)-1)):
                    # appending additions from previous list
                    cur_list.append(prev_list[count] + prev_list[count+1])
                cur_list.append(1)
            prev_list = cur_list
            return_list.append(cur_list)
        return return_list