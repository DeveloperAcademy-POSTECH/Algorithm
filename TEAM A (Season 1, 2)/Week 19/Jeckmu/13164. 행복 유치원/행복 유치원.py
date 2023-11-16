N, K = map(int, input().split())

heights = list(map(int, input().split()))
heights.sort()  # 키 순 정렬

# 바로 옆 사람과의 키 차이를 계산하여 저장.
gaps = []
for i in range(len(heights)-1):
    gaps.append(heights[i + 1] - heights[i])
    
# 차이의 크기 순으로 정렬 후, 가장 큰 K-1개의 차이를 빼고 계산 (Greedy)
gaps.sort()
if K > 1:
    print(sum(gaps[:-(K-1)]))
else:
    print(sum(gaps))