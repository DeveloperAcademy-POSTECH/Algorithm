# 숫자 카드는 정수 하나가 적혀져 있는 카드이다.
# 상근이는 숫자 카드 N개를 가지고 있다.
# 정수 M개가 주어졌을 때, 이 수가 적혀있는 숫자 카드를 상근이가 가지고 있는지 아닌지를 구하는 프로그램을 작성하시오.
#
# import sys
# import bisect
#
# input = sys.stdin.readline
#
# # 갖고 있는 숫자 카드의 개수, 숫자 카드에 적혀 있는 정수
# N = int(input())
# cards = list(map(int, input().split()))
# cards.sort()
# # M 개의 정수
# M = int(input())
# nums = list(map(int, input().split()))
#
# for i in nums:
#     first = bisect.bisect_left(cards, i)
#     last = bisect.bisect_right(cards, i)
#     print(last-first, end=' ')


import sys

input = sys.stdin.readline


# binary search
def BSearch(cards, nums):
    for i in nums:
        first, last = 0, N-1
        isExist = False
        while first <= last:
            mid = (first + last) // 2
            if cards[mid] == i:
                isExist = True
                break
            elif cards[mid] > i:
                last = mid - 1
            else:
                first = mid + 1
        print(1 if isExist else 0, end=' ')


# 갖고 있는 숫자 카드의 개수, 숫자 카드에 적혀 있는 정수
N = int(input())
cards = list(map(int, input().split()))
cards.sort()
# M 개의 정수
M = int(input())
nums = list(map(int, input().split()))

BSearch(cards, nums)
