# given n names and phone numbers,
# assemble a phone book that maps friends' names to their respective phone numbers
# you will then be given an unknown number of names to query your phone book for

# for each name queried, print the associated entry on a new line in the form 'name=phoneNumber'
# if the entry for name is not found, print 'Not found' instead

n = int(input())
phone_number = [input().split() for _ in range(n)]

# dictionary with each name and phone_number input
phone_book = {k: v for k,v in phone_number}

while True:
    try:
        name = input()
        if name in phone_book:
            print('%s=%s' % (name, phone_book[name]))
        else:
            print('Not found')
    except:
        break