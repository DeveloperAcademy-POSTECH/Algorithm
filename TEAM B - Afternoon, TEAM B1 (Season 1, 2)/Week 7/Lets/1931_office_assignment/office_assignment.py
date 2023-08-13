# 회의실 배정
# https://www.acmicpc.net/problem/1931

# 회의 수 < 100,000
# -> NlogN 정도?

# 그리디 알고리즘
# -> 각 순간에서 최선의 답을 탐색함
# -> 이게 전체 최선이기를 바라는 방법
# 근데 말이 되나... 결국 하나씩 다 조사해봐야하는거 아님?

# 활동 선택 문제: 시간표를 최대한 많이 배정하거나 선택하는 문제
# 이러한 문제의 특징은 '하나의 활동을 완료하기 전 까지는 다른 활동을 할 수 없다'
# -> 하나의 활동을 선택하면 나머지 겹치지 않는 활동에 대해서 독립적이고, '탐욕 선택이 이후 결과에 영향을 미치지 않는다'

# 독립적이니까 빠르게 끝나는것들일수록 뒤에 독립적인 상황들이 더 많이 붙을 수 있음
# 그렇기떄문에 끝나는 시간을 기준으로 정렬


# 이 문제에서는 (8,8) 처럼 시작하자마자 끝나는 것도 있을 수 있음
# sort 를 이용할때, 처음 인자에 대해서는 오름 차순, 그 다음 인자에 대해서는 내림차순으로 정렬하고 싶으면 다음과 같이
# f = sorted(e, key = lambda x: (x[0], -x[1]))


import sys
sys.stdin = open("1931_office_assignment/office_assignment.txt", "r")


N = int(sys.stdin.readline())

times = []
for _ in range(N):
    times.append(tuple(map(int, sys.stdin.readline().split())))

times.sort(key = lambda x: (x[1], x[0]))


print(times)

start, end = times[0]

cnt = 1

for i in range(1, len(times)):
    if times[i][0] >= end:
        start, end = times[i]
        cnt += 1

print(cnt)