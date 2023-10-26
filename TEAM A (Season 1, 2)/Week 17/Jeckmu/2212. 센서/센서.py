N = int(input())
K = int(input())

sensor = list(map(int, input().split()))
sensor = sorted(sensor)

gap = []
for i in range(len(sensor)-1):
    gap.append(sensor[i+1] - sensor[i])
    
gap = sorted(gap)
if K != 1:
    print(sum(gap[:-(K-1)]))
else:
    print(sum(gap))