# 백준: 회의실 배정
# https://www.acmicpc.net/problem/11000

# 이 문제도 이전 문제랑 비슷한데 뭐가 다른걸까? 왜 heap 을 써야하지?
# -> 아마 자동으로 가장 빠른 종료시간을 앞으로 끌어오기 위해서인가보다. 계속 sort 를 할 수는 없으니까

# N < 200,000
# Nlog2N -> 2십만 * 18 == 40만정도? 괜찮은데... 흠...
# 수업 끝난 직후 다른 수업 가능
# 최소의 강의실을 사용해서 모든 수업을 가능하게 해야함

# 현재 회의 종료시간과 다음 열린 회의 시작시간과의 관계가 중요함

import sys
import heapq
sys.stdin = open("11000_classroom_assignment/classroom_assignment.txt", "r")

N = int(sys.stdin.readline())

times = []

for i in range(N):
    start, end = list(map(int, sys.stdin.readline().split()))
    times.append((start, end))

times.sort(reverse=True) # 나중에 pop 으로 하나씩 뽑아내기 위해 역정렬

classroom = [] # 종료시간들을 저장할 min heap -> 종료시간이 빠른순서대로 저장됨
heapq.heapify(classroom)
heapq.heappush(classroom, 0)

while times:
    start, end = times.pop()
    if start < classroom[0]: # 현재 가장 빠른 종료시간보다 시작시간이 빠르다? -> 새로운 강의실
        heapq.heappush(classroom, end)
    else:
        heapq.heappop(classroom) # 현재 가장 빠른 종료시간보다 시작시간이 느리다? -> 강의실 교체
        heapq.heappush(classroom, end)

print(len(classroom))

# times = []
# for _ in range(N):
#     times.append(tuple(map(int, sys.stdin.readline().split())))


# times.sort(key=lambda x: (x[1], x[1]-x[0]), reverse = True)

# pos = 0
# classes = []

# while times:
#     start, end = times.pop()
#     # flag = True

#     target_idx = -1
#     min_diff = 200000

#     for i in range(len(classes)):
#         if classes[i][1] <= start:
#             if min_diff > abs(start - classes[i][1]):
#                 target_idx = i
#                 min_diff = abs(start - classes[i][1])
#                 # flag = False
    
#     if target_idx != -1:
#         classes[target_idx] = (start, end)
#     else:
#         classes.append((start, end))

#     # if flag:
#     #     classes.append((start, end))
    

# print(len(classes))


## heapq 를 사용한 풀이
# times = []
# heapq.heapify(times)
# for _ in range(N):
#     start, end = list(map(int, sys.stdin.readline().split()))
#     heapq.heappush(times, (start, end))


# classes = [(0, 0)]
# heapq.heapify(classes)

# stack = []

# while times:
#     start, end = heapq.heappop(times)
#     # print(f"{end} {start}")
#     # print(f"times {times}")
#     flag = True

#     while classes:
#         # print(f"classes {classes}")
#         class_end, class_start = heapq.heappop(classes)

#         if class_end <= start:
#             heapq.heappush(classes,(end, start))
#             flag = False
#             break
#         else:
#             stack.append((class_end, class_start))

#     if flag:
#         heapq.heappush(classes, (end, start))

#     # print(f"stack {stack}")
#     while stack:
#         heapq.heappush(classes, stack.pop())
    
#     # print(f"classes:{classes} stack:{stack}")
#     # print("-"*20)
# print(len(classes))