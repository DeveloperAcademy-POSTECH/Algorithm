# 2805 나무 자르기
# 나무 M미터
# 목재 절단기 - 높이 H 지정해서 자름(양의 정수, 0)
# ex) 한 줄에 있는 나무가 20, 15, 10, 17이고, 높이가 15라면,
# 잘린 나무의 높이: 15, 15, 10, 15
# -> 상근이는 5,2 나무를 들고 집에 간다.
# => 최소한 M 미터를 들고 집에 갈거야. 높이의 최댓값을 구해

import sys

input = sys.stdin.readline

#이진탐색
# 높이 = target
def BSearch(tree, first, last, M):
    while first <= last:
        target = 0
        mid = int((first + last) / 2)
        for i in tree:
            if(i > mid):
                target += i - mid
        if target >= M:
            first = mid + 1
        else:
            last = mid - 1
    return last


# N개의 나무, M의 나무를 집에 가져가
N, M = map(int, input().split())

tree = list(map(int, input().split()))

print(BSearch(tree, 1, max(tree), M))