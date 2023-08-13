
n = int(input())
 
arr = []
for _ in range(n):
    age, name = input().split()
    arr.append([int(age),name]) # 2차원 리스트에 입력값 저장
 
arr.sort(key=lambda x:int(x[0])) # 오름차순 정렬 / lambda함수를 통해 첫번째 요소만 정렬 (lamda: 함수를 한 줄로 만들어줌)
 
for i in arr:
    print(i[0],i[1])
