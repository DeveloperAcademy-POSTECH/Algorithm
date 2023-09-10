# 1912 연속합
# https://www.acmicpc.net/problem/1912

# 1초
# N 개의 정수로 이루어진 임의의 수열 중 연속된 몇개의 수를 선택해서 구할 수 있는 합 중 가장 큰 합

# N < 100,000

# 최대 연속 부분합
# 힌트: https://ssungkang.tistory.com/entry/Algorithm-%EC%97%B0%EC%86%8D-%EA%B5%AC%EA%B0%84%EC%9D%98-%EC%B5%9C%EB%8C%80-%ED%95%A9-%EA%B5%AC%ED%95%98%EA%B8%B0
# dp(i) 라는 점화식을 arr[i] 를 오른쪽 끝으로 하는 구간의 최대합이라고 생각
# dp(i) 는 'dp(i-1) + arr[i]' 또는 'arr[i] 독자적인 값' 둘 중 하나

# 왜 독자적인 값일까? 

# 이 arr[i] 를 더했을때 dp[i] 까지의 합이 0보다 크다면, i 번쨰 이후에도 숫자들을 더하면서 최대가 될지 안될지를 확인해도 된다.
# e.g) 3, 6, 2, -5 라고 했을때 -5 를 더해도 양수니까 아예 안더하는것보다는 나으니까
# 그러나 arr[i] 를 더했을때 부분 수열의 합이 음수가 된다면, 더는 볼 필요가 없다. i 번째 이후부터 새로 시작하는게 낫다
# e.g) 3, 6, 2, -20 라고 했을때 다 더했을때 -9니까 오히려 이 수열을 더하면 손해임. 따라서 그냥 0으로 깔끔하게 다시 세팅하고 i+1번쨰 이후를 탐색
# 이때 i+1 번쨰 값 독자적인 값으로 새로운 부분수열에 들어가게 됨



import sys
sys.stdin = open("1912_consecutiveSum/consecutiveSum.txt", "r")
input = sys.stdin

N = int(input.readline())
numbers = list(map(int, input.readline().split()))

currentPartialSum = -1000
maxVal = -1000

print(numbers)
for i in range(N):
    currentPartialSum = max(currentPartialSum + numbers[i], numbers[i]) # 이 부분이 위에서 길게 설명해놓은 부분합 + arr[i] 또는 독자적인 값
    maxVal = max(currentPartialSum, maxVal) # maxVal 을 업데이트 해주기

print(maxVal)
