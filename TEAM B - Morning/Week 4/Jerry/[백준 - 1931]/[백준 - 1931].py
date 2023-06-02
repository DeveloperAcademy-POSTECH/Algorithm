#1931 백준

n = int(input())
room = []

for i in range(n):
    a, b = map(int, input().split())
    room.append([a, b])
# 최대 회의의 갯수와 시작 종료시간을 모두 받음.

room.sort(key = lambda x: x[0])
room.sort(key = lambda x: x[1])
# 시작시간 기준으로 정렬 -> 그후 종료시간 기준으로 정렬.
# 꼬리 잡기형식으로 값을 찾아 나갈껀데 처음시작시간의 종료시간-> 종료시간에서 다음의 시작시간식으로 찾아 나갈 것이기에
# 중간의 시작시간이 버려지면 안되기에


cnt = 1 #시작된 회의수 1개
end = room[0][1] # 시작된 회의의 종료시간
for i in range(1, n):
    if room[i][0] >= end: # 가능한 다음 회의를 찾으면
        cnt += 1
        end = room[i][1] # 그회의의 종료시간을 채택, 회의수 1 추가

print(cnt)