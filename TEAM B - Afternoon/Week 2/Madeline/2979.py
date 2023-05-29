# 2979

#정수 여러개 입력받기
A, B, C = map(int, input().split())
#시간별로 차 개수 * 금액
truck = [0]*100
fee = 0
for _ in range(3):
    enter, left = map(int, input().split())
    for i in range(enter, left):
        truck[i] += 1

for j in truck:
    if(j == 1):
        fee += A * j
    elif(j == 2):
        fee += B * j
    elif(j==3):
        fee += C * j
print(fee)