n = int(input())
arr = list(map(int, input().split()))

#dp테이블 초기화
d = [0]*100 #d는, 만약 해당 인덱스까지만 있다고 할때, 그 인덱스 기준의 최적값.

#보텀업 방식의 dp 진행 (왼쪽 식량창고부터 털지 안 털지 결정)

d[0] = arr[0]
d[1] = max(arr[0],arr[1])

for i in range(2,n):
    d[i] = max(d[i-1],d[i-2]+arr[i])

#최종적으로, n개의 식량창고를 터는 경우의 최적값은 d[n-1]
print(d[n-1])


