n = int(input())
meetings = []

for i in range(n):
    startTime, endTime = map(int, input().split())
    meetings.append([startTime,endTime])

meetings.sort(key=lambda x: (x[1],x[0]))

lastEndTime = 0
answer = 0

for start, end in meetings:
    if start >= lastEndTime:
        lastEndTime = end
        answer += 1

print(answer) 