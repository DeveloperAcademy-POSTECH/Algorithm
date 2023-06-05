# https://www.acmicpc.net/problem/2343
# 백준-2343-기타 레슨
import sys

n, m = map(int, sys.stdin.readline().split())
videos = list(map(int, sys.stdin.readline().split()))

total_length = sum(videos)
min_length = total_length // m if total_length % m == 0 else total_length // m + 1
print(min_length)
max_temp_sum = 0
temp_sum = 0
for video in videos:
    temp_sum += video
    print(temp_sum)
    if temp_sum >= min_length:
        max_temp_sum = max(max_temp_sum, temp_sum)
        temp_sum = 0
        
print(max_temp_sum)