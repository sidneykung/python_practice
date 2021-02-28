# https://leetcode.com/problems/can-place-flowers/

# You have a long flowerbed in which some of the plots are planted, and some are not. 
# However, flowers cannot be planted in adjacent plots.

# Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, return if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule.

# example 1
# input: flowerbed = [1,0,0,0,1], n = 1
# output: true

# example 2
# input: flowerbed = [1,0,0,0,1], n = 2
# output: false

class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        if n == 0:
	    return True

        flowerbed = [0] + flowerbed + [0]
        current = 1
        while current < len(flowerbed)-1:
	        if flowerbed[current-1] == 0 and flowerbed[current] == 0 and flowerbed[current+1] == 0:
		        flowerbed[current] = 1
		        n -= 1
		        if n == 0:
		    	    return True        
	        current += 1
        return False