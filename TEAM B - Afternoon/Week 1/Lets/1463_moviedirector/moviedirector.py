# 종말의 수 -> 어떤 수에 6이 적어도 3개 이상 연속으로 들어가는 수
# 666, 1666, 2666, 3666, ...
# n 번째 종말의 수를 찾아보자
# 일단은 어떤 숫자가 6이 3연속으로 들어가는지 판별하는 함수가 필요하겠네



import sys
sys.stdin = open("1463_moviedirector/moviedirector.txt", "r")

N = int(sys.stdin.readline())


# 6이 3연속으로 들어가는지 확인하는 함수
def check_end_number(n):
    str_num = str(n) # 받아온 숫자를 문자열로 치환한 후

    for i in range(len(str_num)-2): 
        if str_num[i] == "6": # 6이 나온 인덱스부터 그 뒷, 뒷뒷 인덱스까지를 조사
            if str_num[i+1] == "6" and str_num[i+2] == "6":
                return True # 666이면 True 
    
    return False # 끝날때까지 못찾으면 False

cnt = 0
num = 665 # 가장 첫 종말의 수 직전의 수인 665 에서 시작

while cnt < N:
    num += 1 # cnt 조건이 맞으면 loop 를 탈출하는데, 탈출할때 num+=1 을 해버리면 연산한값에서 +1된 값이 나오므로 그냥 아예 초반에 +1 을 해줌
    if check_end_number(num) == True:
        cnt += 1

print(num)
    


