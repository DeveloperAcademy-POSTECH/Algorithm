# 정확히 N 킬로그램의 설탕을 배달
# 설탕은 5킬로봉지와 3킬로봉지가 있음
# 최대한 적은 봉지를 들고 가려고 함
# N 킬로그램을 배달할때, 최소로 들고가는 봉지수를 구하라
# 만약 정확하기 N 킬로그램을 만들 수 없다면, -1


# 음... 일단 감이 잘 안잡힌다
# 18을 예로 했을때를 생각해보면, 
# 일단은 15가 넘지않는 가장 가까운 5의 배수니까 15까지는 5킬로
# 그 뒤를 3킬로로 채우는게 내 머리속의 동작방식인데, 이대로 해볼까
# 아니면 5를 더하던지 3을 더하던지를 계속 가지치기로 나누는 방식으로 해서 내려가는 방식도 괜찮을듯?
# -> 아 근데 이거는 재귀를 너무 많이 내려가서 에러남... 백준에서는 1000번까지만 내려가기 가능 근데 input 이 5000번임 ㅋ...
# 함수 아니라 while 문이나 for 문으로 만들어볼까
# 다시 방법1로 가서 5로 채우고, 하나 뺴고 3으로 채우고, 그래도 안되면 또 하나빼고 3으로 채우고 반복하자

import sys
sys.stdin = open("2839_sugardelivery/sugardelivery.txt", "r")

N = int(sys.stdin.readline())


def sugar_bags():
    current_weight = 0 # 현재까지 쌓은 설탕의 무게
    bag5_num = 0 # 5킬로 설탕의 갯수
    bag3_num = 0 # 3킬로 설탕의 갯수
    max_bag_num = (N // 3) + 1 # 3킬로로 다 채워도 이것보다는 적어야함

    if N % 5 == 0: # 바로 5로 나눠 떨어지면 그게 최소 갯수
        return N // 5
    else: 
        bag5_num = (N // 5) + 1 # 해당 킬로수와 가장 가까운 상위 5의 배수를 찾음

        for i in range(bag5_num-1, -1, -1): # 가장 5킬로가 많은 경우부터 내려감
            current_weight = i * 5

            while current_weight < N: # 무게랑 딱 맞거나 약간 오버할때까지 3킬로 설탕을 계속 쌓음
                # print(current_weight, i, bag3_num)
                bag3_num += 1
                current_weight += 3
            
            if current_weight == N: # 킬로그램이 맞았을때
                # print(i, bag3_num)
                return i + bag3_num
            
            if bag3_num >= max_bag_num: # 최대보다 3킬로 설탕을 더 쌓았다? -> 도달할 수 없는 수
                return -1
            
            bag3_num = 0 # 매번 3킬로 설탕은 다시 0개부터 쌓는거니까 초기화

# sugar_bags()
print(sugar_bags())


# min_bags = 5000 # 설탕봉지의 최소갯수
# flag = False # 3, 5킬로짜리 설탕봉지로 가능하면 True 로 바꿔줌

# sys.setrecursionlimit(10**6)
# def add_sugar(current_weight, bag_cnt):
#     if current_weight > N: # 현재 무게가 초과했으면 탈출
#         return
    
#     global min_bags, flag
#     if bag_cnt >= min_bags: # 설탕 봉지수가 최소랑 같거나 초과하면 탈출
#         return
    
#     if current_weight == N: # 설탕 킬로수를 맞췄으면
#         flag = True
#         min_bags = min(min_bags, bag_cnt) # 현재가 최소면 min_bags 값을 바꿈
#         return
    
#     add_sugar(current_weight+3, bag_cnt+1)
#     add_sugar(current_weight+5, bag_cnt+1)

# add_sugar(0, 0)

# if flag:
#     print(min_bags)
# else:
#     print(-1)