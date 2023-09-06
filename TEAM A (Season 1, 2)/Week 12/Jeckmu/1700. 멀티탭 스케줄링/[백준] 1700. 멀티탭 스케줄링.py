from collections import deque
import sys
read = sys.stdin.readline


def index(x):
    if x not in elecs:
        return -1
    else:
        return elecs.index(x)


N, k = map(int, read().strip("\n").split())
elecs = list(map(int, read().strip("\n").split()))

tap = deque([])
eleclist = elecs[:]
elecs = deque(elecs)
answer = 0

for elec in eleclist:
    if elec in tap:
        elecs.popleft()
        continue
    elif len(tap) < N:
        tap.append(elecs.popleft())
    else:
        lastindex = 0

        for n in tap:
            j = index(n)
            if j == -1:
                tap.remove(n)
                lastindex = -1
                break
            else:
                if j > lastindex:
                    lastindex = j

        if lastindex != -1:
            tap.remove(elecs[lastindex])

        tap.append(elecs.popleft())
        answer += 1

print(answer)
