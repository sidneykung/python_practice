# https://www.codewars.com/kata/56269eb78ad2e4ced1000013/python
# Return the next square if sq is a square, -1 otherwise


def find_next_square(sq):
    n = sq**(0.5)
    if n.is_integer():
        return (n+1)**2
    else:    
        return -1