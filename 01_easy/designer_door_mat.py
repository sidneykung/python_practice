# https://www.hackerrank.com/challenges/designer-door-mat/problem

# solution:

# height
N,M = map(int, input().split())

# top triangle
# start 1, end N, step 2
for i in range(1, N, 2):
    print(str('.|.' * i).center(M, '-'))
# middle
print('WELCOME'.center(M,'-'))
# bottom triangle
for i in range(N-2, -1, -2):
    print(str('.|.' * i).center(M, '-'))
