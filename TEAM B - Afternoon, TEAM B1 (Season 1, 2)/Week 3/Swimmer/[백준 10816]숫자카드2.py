# 이진탐색 함수

def binary_search (arr, target, start, end) :
    if start > end :
        return None
    
    mid = (start+end)//2
    
    if target == arr[mid]:
        return mid
    
    elif target < arr[mid]:
        return binary_search(arr, target, start, mid-1)

    else :
        return binary_search(arr, target, mid+1, end)


# 입력 받기
n = int(input())
numbercardlist = list(map(int, input().split()))
m = int(input())
numbertocountlist = list(map(int, input().split()))

# 숫자카드 리스트를 sort
numbercardlist.sort()

# 크기가 m인 0으로 이루어진 빈 배열 result 선언.

result = [0 for _ in range(0,m)]

for i in range(0,m):
    while binary_search(numbercardlist, numbertocountlist[i], 0, len(numbercardlist)-1) != None:
        numbercardlist.pop(binary_search(numbercardlist, numbertocountlist[i], 0, len(numbercardlist)-1))
        result[i] += 1

print(*result)
