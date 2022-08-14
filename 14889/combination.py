import sys
import itertools

N = int(input())
M = []
for i in list(range(N)):
    M.append(list(map(int,sys.stdin.readline().split())))

T = [ i for i in list(range(N))]
PT = list(itertools.combinations(T, N//2))

diff = 1e9

for teamA in PT:
    teamASum = 0
    for i in list(range(N//2)):
        member = teamA[i]
        for j in teamA:
            teamASum += M[member][j]
        
    teamB = tuple(set(T) - set(teamA))
    teamBSum = 0
    for i in list(range(N//2)):
        member = teamB[i]
        for j in teamB:
            teamBSum += M[member][j]
    
    diff = min(diff, abs(teamASum - teamBSum))

print(diff)