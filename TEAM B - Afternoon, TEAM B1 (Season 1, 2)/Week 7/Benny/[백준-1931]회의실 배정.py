import sys

input = sys.stdin.readline

n = int(input())
meetings = []
for _ in range(n):
    meetings.append(list(map(int, input().split())))

meetings.sort(key=lambda x: (-x[1], -x[0]))
cur = meetings.pop()
count = 1
while meetings:
    temp = meetings.pop()
    if temp[0] >= cur[1]:
        cur = temp
        count += 1

print(count)