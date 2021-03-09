# regex password validation
# https://www.codewars.com/kata/52e1476c8147a7547a000811/python

regex = '^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[^\W_]{6,}$'

# ^                  begin string
# (?=.*[a-z])        at least 1 lowercase
# (?=.*[A-Z])        at least 1 uppercase
# (?=.*\d)           at least 1 digit
# [^\W_]             only alphanumeric
# {6,}               at least 6 characters long
# $                  end string