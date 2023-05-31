# 해당 좌표보다 작은 좌표의 갯수를 출력하면 되는듯허이
# N <= 1,000,000
# -10^9 < Xi < 10^9 -> 괴랄함, 이분탐색을 생각하자

# 일단 이 문제도 dict 가 먼저 떠오르는데 그래도 이진탐색으로 풀어보자
# 이 문제는 겹치는 숫자가 나올 수 있음 -> set 에 넣어서 겹치는건 줄여야할듯

import sys
sys.stdin = open("18870_coordinateCompress/coordinateCompress.txt", "r")

N = int(sys.stdin.readline())
given_numbers = list(map(int, sys.stdin.readline().split())) # 원본 숫자들
compressed_numbers = list(set(given_numbers[:])) # set 로 압축한 숫자들
compressed_numbers.sort() # 오름차순 정렬

def binary_search(n): # 이진탐색 함수
    start = 0
    end = len(compressed_numbers) -1 # 이진탐색하는 대상이 compressed_numbers 인데 여기서 그냥 N 갖다 썼다가 index error 났다 멍청이

    while start <= end:
        mid = (start + end) // 2
        if compressed_numbers[mid] == n:
            return mid
        else:
            if compressed_numbers[mid] > n:
                end = mid - 1
            else:
                start = mid + 1

answer = []
for number in given_numbers:
    answer.append(str(binary_search(number)))

print(" ".join(answer))
