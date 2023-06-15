# 백준-2805-나무 자르기
# https://www.acmicpc.net/problem/2805
import sys

def get_wood(trees, height):
    wood = 0
    for tree in trees:
        if tree > height:
            wood += tree - height
    
    return wood

n, m = map(int, sys.stdin.readline().split())
trees = list(map(int, sys.stdin.readline().split()))
    
left, right = 0, max(trees)

answer = 0
while left <= right:
    mid = (left + right) // 2
    wood = get_wood(trees, mid)
    if wood < m:
        right = mid - 1
    elif wood == m:
        answer = mid
        break
    else:
        answer = max(answer, mid)
        left = mid + 1
        
print(answer)