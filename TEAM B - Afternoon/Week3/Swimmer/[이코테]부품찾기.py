
# 이진탐색 함수

def binary_search(arr, target, start, end):
    if start > end :
        return None
    mid = (start+end)//2
    if target == arr[mid] :
        return mid
    elif target < arr[mid] :
        return binary_search(arr, target, start, mid-1)
    else  :
        return binary_search(arr, target, mid+1, end)

# N (= 가게의 부품 개수), storelist (= 가게의 부품번호 리스트) 받기

n = int(input())
storelist = list(map(int, input().split()))

# M (= 확인 요청한 부품의 개수), requestlist (= 확인 요청받은 부품의 리스트) 받기

m = int(input())
requestlist = list(map(int, input().split()))

# requestlist의 item들에 대해서 순차적으로 이진탐색 진행 및 print

for i in range (0,m) :
    if binary_search(storelist, requestlist[i], 0, n-1) == None :
        print("no", end=" ")
    else :
        print("yes", end=" ")
