# N 개의 정수가 주어져있을떄, 이 안에 X 라는 정수가 존재하는지 알아내는 프로그램

# N <= 100,000, M <= 100,000
# N 개의 수 중에서 M 개의 숫자들이 각각 존재하는지 찾기
# 정수의 범위가 - 2^31 ~ 2^31 -> 개큼, 그리고 뭔가 이진탐색의 느낌이 나는 수

# 가장 처음으로 머리에 떠오른 생각은 dict 로 풀면 안되나?
# 그래도 이진탐색 분야이니 이진탐색으로 풀어보자

import sys # 입력받기
sys.stdin = open("1920_findNumber/findNumber.txt", "r")

N = int(sys.stdin.readline())
have_numbers = list(map(int, sys.stdin.readline().split()))

M = int(sys.stdin.readline())
given_numbers = list(map(int, sys.stdin.readline().split()))

# 1. 이진 탐색으로 풀어보자 -> 성공, 408ms
have_numbers.sort() # 우선 오름차순 정렬

def binary_search(n): # 이진탐색 함수
    start = 0
    end = N - 1
    while start <= end:
        mid = (start + end) // 2 # mid 설정
        observing_number = have_numbers[mid] # 현재 관찰하는 숫자 설정

        if observing_number == n: # 관찰하는 숫자가 찾는 숫자면 1 반환
            return 1
        else:
            if observing_number > n: # 관찰하는 숫자가 찾는 숫자보다 크다? -> mid 를 낮춘다 -> end 를 끌어내린다
                end = mid - 1
            else: # 관찰하는 숫자가 찾는 숫자보다 작다? -> mid 를 높힌다 -> start 를 끌어올린다.
                start = mid + 1 
    return 0

for number in given_numbers:
    print(binary_search(number))


# 2. dict 로 풀어보자 -> 성공, 188ms
# number_dict = {}
# for number in have_numbers:
#     if number_dict.get(number) == None:
#         number_dict[number] = True

# for number in given_numbers:
#     if number_dict.get(number) != None:
#         print(1)
#     else:
#         print(0)
