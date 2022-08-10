import itertools
import collections

def getNumberfromWord (words, weights):
    numberString = ''
    for word in words:
        numberString += str(weights[word])

    return numberString

count = int(input())
sum = 0
sentences = []
wordSet = set()
wordDict = collections.defaultdict(int)
weightDict = collections.defaultdict(int)
for i in range(count):
    curr = input()
    length = len(curr)
    for idx, c in enumerate(curr):
        if length -idx > wordDict[c]:
            wordDict[c] = length-idx
    sentences.append(curr)


total = len(wordDict.keys())
numbers = list(range(9,9-total,-1))
weights = sorted(list(wordDict.items()), key=lambda x:x[1])[::-1]


for k, weight in weights:
    wordDict[k] = numbers[0]
    numbers.pop(0)



        
for sentecne in sentences:
    sum += int(getNumberfromWord(sentecne, wordDict))

print(sum)





