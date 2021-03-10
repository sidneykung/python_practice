# Help the Fruit Guy
# https://www.codewars.com/kata/557af4c6169ac832300000ba

# Your task is to implement a method that accepts an array of strings containing fruits should return an array of strings where all the rotten fruits are replaced by good ones.

# Note:
# If the array is null/nil/None or empty you should return empty array ([]).
# The rotten fruit name will be in this camelcase (rottenFruit).
# The returned array should be in lowercase.

def remove_rotten(bag_of_fruits):
    if not bag_of_fruits:
        return []
    else:
        return list(map(lambda x: x.replace('rotten','').lower() , bag_of_fruits))