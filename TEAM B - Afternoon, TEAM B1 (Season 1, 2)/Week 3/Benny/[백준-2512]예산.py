# https://www.acmicpc.net/problem/2512
# 백준-2512-예산
import sys

def get_amount(requests, upper):
    amount = 0
    for req in requests:
        amount += min(req, upper)
        
    return amount

n = int(sys.stdin.readline())
requests = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())

left, right = 1, max(requests)
answer = 1
while left <= right:
    mid = (left + right) // 2
    amount = get_amount(requests, mid)
    if amount < m:
        answer = max(answer, mid)
        left = mid + 1
    elif amount == m:
        answer = mid
        break
    else:
        right = mid - 1
        
print(answer)