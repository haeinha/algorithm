import sys
import itertools

flag = False

while True:
    temp = list(map(int, sys.stdin.readline().split()))
    if temp[0] == 0:
        break
    
    # if flag:
    #     print('\n')
    # else:
    #     flag = True
    N = temp[0]
    M = temp[1:]

    for li in list(itertools.combinations(M, 6)):
        print(' '.join([str(x) for x in li]), sep='\n')
    print()