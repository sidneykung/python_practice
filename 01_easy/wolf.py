# https://www.codewars.com/kata/5c8bfa44b9d1192e1ebd3d15/train/python

# Warn the sheep in front of the wolf that it is about to be eaten. Remember that you are standing at the front of the queue which is at the end of the array:

# If the wolf is the closest animal to you, return "Pls go away and stop eating my sheep". Otherwise, return "Oi! Sheep number N! You are about to be eaten by a wolf!" where N is the sheep's position in the queue.

# example:
# Input: ["sheep", "sheep", "sheep", "wolf", "sheep"]
# Output: "Oi! Sheep number 1! You are about to be eaten by a wolf!"

def warn_the_sheep(queue):
    wolf = len(queue) - queue.index('wolf') - 1
    return f'Oi! Sheep number {wolf}! You are about to be eaten by a wolf!' if wolf else 'Pls go away and stop eating my sheep'