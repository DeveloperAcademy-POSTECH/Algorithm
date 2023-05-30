
# 나의 개수 n, 요청받은 길이 m을 입력받기
n, m = map(int,input().split())

# 나의 길이 list를 입력받기
array = list(map(int, input().split()))

start = 0
end = max(array)

maxheight = 0  # 최종 결과 값인 maxheight를 전역변수로 선언.

# 이진탐색을 통해 maxheight 구하기

while start <= end :
    total = 0
    mid = (start+end) // 2
    for item in array : # array 안의 나의 길이가 mid 보다 클 경우, 잘린 길이의 크기를 sum 하기.
        if item > mid :
            total += item - mid
    if total < m : # total의 크기가 요청받은 나의 길이 m보다 작을 경우 => height을 줄여야 함으로 end를 감소.
        end = mid -1
    else : # total의 크기가 요청받은 나의 길이보다 크거나 같을 경우 => 이때의 mid가 maxheight일 가능성이 있기 때문에 일단 maxheight에 할당. 그 다음 start 증가.
        maxheight = mid
        start = mid+1


print(maxheight)
