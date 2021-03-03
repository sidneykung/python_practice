# 1. is_even
# Define a function is_even that will take a number x as input.
# If x is even, then return True.
# Otherwise, return False

def is_even(x):
  if x%2 == 0:
    return True
  else:
    return False

print is_even(5)  # False
print is_even(6)  # True

# 2. is_int
# Define a function is_int that takes a number x as an input.
# Have it return True if the number is an integer and False otherwise.

def is_int(x):
  if x%1 == 0:
    return True
  else:
    return False

is_int(7.0)   # True    
is_int(7.5)   # False    
is_int(-1)    # True   