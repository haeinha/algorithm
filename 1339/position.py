import itertools
import collections

count = int(input())
sum = 0
sentences = []
wordSet = set()
weightDict = collections.defaultdict(int)
for i in range(count):
    curr = input()
    length = len(curr)
    for idx, c in enumerate(curr):
        weightDict[c] += 10 ** (length-idx-1)

    sentences.append(curr)


total = len(weightDict.keys())
numbers = list(range(9,9-total,-1))
weights = sorted(list(weightDict.items()), key=lambda x:x[1])[::-1]


number = 9
i = 0
sum = 0
for k, weight in weights:
    sum += weight * (number - i)
    i+=1
    


print(sum)





