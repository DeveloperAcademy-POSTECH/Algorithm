#백준-2559-수열
#https://www.acmicpc.net/problem/2559

import sys

input = sys.stdin.readline

n, k = map(int, input().split())
temps = list(map(int, input().split()))

temp_value = sum(temps[0:k])
max_value = temp_value
for i in range(1, n-k+1):
    temp_value += temps[i+k-1] - temps[i-1]
    max_value = max(max_value, temp_value)
    
print(max_value)

'''
N-K번 순회하면서 sum을 구할 경우, K*(N-K)번 필요 -> K는 aN (0<a<=1)로 고쳐쓸 수 있음.
따라서 aN^2-a^2N^2가 됨. 이는 빅오 표기법으로 O(N^2)이 됨.
이 때 sum이 아니라 부분합의 왼쪽 끝값을 빼고 오른쪽 끝값을 더하는 식으로 한다면 더하기 연산을
K번이 아닌 2번으로 줄일 수 있음 이는 곧 2*(N-K)번의 연산횟수이므로 빅오표기법으로 O(N)이 됨.
'''