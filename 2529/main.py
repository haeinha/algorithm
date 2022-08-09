import itertools

k = int(input())
inEqulityList = input().split()

arr = list(itertools.permutations(range(0,10), k+1))

min, max = '9999999999', '0'
def compare(a, b, inequality):
    return  a < b if inequality == '<' else a > b

flag = True
for tup in arr:
    for i in range(k):
        if compare(tup[i], tup[i+1], inEqulityList[i]):
            continue
        else :
            flag = False
            break
    
    if flag :
        current = ''.join(str(x) for x in tup)
        if int(min) > int(current):
            min = current
        if int(max) < int(current):
            max = current
    
    flag = True

print(max, min, sep='\n')
