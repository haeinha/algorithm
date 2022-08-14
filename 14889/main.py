import sys
import itertools

N = int(input())
M = []
for i in list(range(N)):
    M.append(list(map(int,sys.stdin.readline().split())))

fM = list(itertools.chain(*M))

O = [0]*(N*N//2) + [1]*(N*N//2)
OP = itertools.permutations(O)
MIN = 1e9

for permutation in OP:
    one = 0
    zero = 0
    for key, value in enumerate(permutation):
        if value == 0:
            one+=fM[key]
        else:
            zero+=fM[key]
    
    if MIN > abs(one - zero):
        MIN = abs(one - zero)

print(MIN)



          



