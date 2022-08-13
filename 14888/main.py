import itertools
import sys

N = int(input())
M = list(map(int,sys.stdin.readline().split()))
O = list(map(int,sys.stdin.readline().split()))
max = 10 ** 9 * -1
min = 10 ** 9

Olist = ''
Operators = ['+', '-', '*', '/']

def compute (a, b, operator):
    result = 0
    if operator == '+':
        result = a+b
    elif operator == '-':
        result = a-b
    elif operator == '*':
        result = a*b
    elif operator == '/':
        result = a//b if a >= 0 else -a//b * -1
    
    return result

for idx, v in enumerate(O):
    Olist += Operators[idx]*v

permutationList = itertools.permutations(Olist, len(Olist))

for permutation in permutationList:
    result = M[0]
    # print(permutation)
    for idx, value in enumerate(permutation):
        result = compute(result, M[idx+1], value)
    
    # print(result)
    
    if result > max :
        # print("result > max", result, max)
        max = result
        if min == 10 ** 9:
            min = max
    elif result < min:
        # print("result < min", result, min)
        min =result


print(max, min, sep='\n')
        
