
n, m, k = map(int,input().split()) # 리스트의 크기, 더해야할 수의 개수, 같은 인덱스의 수가 연속될수 있는 개수 제한
data = list(map(int, input().split()))

# 배열의 아이템 중 가장 큰 수와 가장 작은 수 찾기
data.sort() # 오름차순 정렬
first = data[n-1]
second = data[n-2]

# first*k + second가 한 조

itt = m // (k+1) # 반복할 수 있는 개수
remain = m % (k+1) # 이 수만큼 first를 곱한 값을 더하기

result = itt * (first*k + second) + (remain*first)

print(result)

