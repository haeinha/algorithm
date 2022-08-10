import itertools

def getNumberfromWord (permutation, words, wordList):
    numberString = ''
    for word in words:
        numberString += str(permutation[wordList.index(word)])

    return numberString

count = int(input())
sentences = []
wordSet = set()
for i in range(count):
    curr = input()
    sentences.append(curr)
    wordSet = wordSet | set(curr)

total = len(wordSet)
wordList = list(wordSet)
numbers = range(9,9-total,-1)

permutations = list(itertools.permutations(numbers,total))

max = 0
for permutation in permutations:
    sum = 0
    for sentence in sentences:
        sum += int(getNumberfromWord(permutation, sentence, wordList))
    
    if sum > max:
        max = sum

print(sum)



