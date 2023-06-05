import sys
input = sys.stdin.readline
N = int(input())
tasklist = [tuple(map(int,input().split())) for _ in range(N)]
tasklist.sort(reverse=True, key= lambda x : x[1])
work = [0 for _ in range(1000)]
for i in range(N):
    for j in range(tasklist[i][0]-1, -1, -1):
        if work[j] == 0:
            work[j] = tasklist[i][1]
            break
print(sum(work))