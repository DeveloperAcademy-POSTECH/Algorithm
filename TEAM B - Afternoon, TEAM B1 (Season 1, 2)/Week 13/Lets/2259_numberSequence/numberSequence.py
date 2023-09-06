# 1초
# 수열의 길이 2 <= N <= 100,000
# 연속한 k 개의 숫자의 합이 최대인 값을 출력
# 일단 그냥 해보자
# -> 시간초과가 나네
# 그러면 어떤 알고리즘을 넣어야할까?
# 아 어짜피 처음 연산하고 하나의 인덱스만 옮기면서 더하고 빼면 되니까 그 방법으로 해보자

# 푼 시간: 28분 30초
# 추가적인 도움: x


import sys
sys.stdin = open("2259_numberSequence/numberSequence.txt", "r")
input = sys.stdin

N, K = list(map(int, input.readline().split()))

numbers = list(map(int, input.readline().split()))

start = 0
end = start + K

maxValue = 0
currentValue = 0

for i in range(start, end):
    currentValue += numbers[i]


maxValue = currentValue



while end < N:
    tempValue = currentValue
    tempValue -= numbers[start]
    tempValue += numbers[end]
    currentValue = tempValue

    maxValue = max(maxValue, tempValue)

    start += 1
    end += 1


print(maxValue)