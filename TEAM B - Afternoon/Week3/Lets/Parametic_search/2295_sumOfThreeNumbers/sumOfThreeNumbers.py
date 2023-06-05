# 자연수로 이뤄진 집합 U
# 이 중에서 적당한 3개의 숫자를 골랐을때 그 합도 U 안에 포함
# 이 경우 중 가장 큰 세 수의 합을 찾자

# U 의 원소 <= 200,000,000, 근데 시간제한 1초? -> 괴랄하니까 이분탐색
# 근데 이분탐색을 어떻게 씀 여기서?
# 일단 U 의 원소의 갯수가 괴랄하니까 여기에다가 이분탐색을 갈겨야하는것 같은데...
# 아 혹시 start, mid end 를 다 더해보는건가? 그래서 안에 있으면 합격인...
# 해보자잇
# 안되는구만
# 그렇다고 itertool 쓰기에는 2억개를 3개 combination 해도 너무 많은데.. 흠...

import sys
sys.stdin = open("2295_sumOfThreeNumbers/sumOfThreeNumbers.txt", "r")

N = int(sys.stdin.readline())

U = []
for _ in range(N):
    U.append(int(sys.stdin.readline()))

U.sort() # 이진 탐색의 첫번쨰 조건

def binary_search():
    start = 0
    end = N - 1
    mid = (start + end) // 2
    answer = ()
    max_val = max(U)
    
    
    while start < end:
        if mid == start or mid == end:
            print("escape!")
            return answer
        
        
        
        target = U[start] + U[mid] + U[end]
        print(start, mid, end)
        print(target)

        if target in U:
            answer = (start, mid, end)
            start = mid + 1
        else:
            if target > max_val:
                end = mid - 1
            else:
                start = mid + 1

        mid = (start + end) // 2
        
    return answer

print(binary_search())
