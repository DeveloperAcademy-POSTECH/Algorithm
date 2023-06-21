N = int(input())
A = set(map(int, input().split()))	# 탐색 시간을 줄이기 위해 set으로 받음
M = int(input())
arr = list(map(int, input().split()))

for i in range(M):
    if arr[i] in A:
        print("1")
    else:
        print("0")


