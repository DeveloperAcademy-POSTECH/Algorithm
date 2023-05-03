# 블랙잭: 카드의 합이 21을 넘지않도록 최대한 크게 만드는 게임
# 새로운 버전
# 양수가 쓰여있는 N 장의 카드를 바닥에 놓음
# 그 후 숫자 M 을 외치면 N 장의 카드 중 3장을 골라 M 을 넘지 않도록 최대한 가까운 수를 만들어야함
 

# 처음 생각
# 1.  M 을 가역변수로 놓고
# 2. 큰 수부터 가역변수에서 빼면서 for 문을 N 장의 카드를 한번 돈다.
# 3. 3장 선택이 끝나면 break
# -> 근데 이건 그리디 방식이라 최적해가 안나옴
# -> 결국 전부 다 검사해봐야하는 결론
# combination 을 쓸까? -> 아 근데 입력값이 30만이면 combination 을 하면 개많을듯
# 그냥 재귀함수로 구현을 하자
# shit... 이게 더 복잡한데.. 그냥 3중 for 문?
# 100 * 100 * 100 해도 1초 안에 끝나긴 하니까 함 해보자 

import sys
# from itertools import combinations

sys.stdin = open("2798_blackjack/blackjack.txt", "r")

N, M = list(map(int, sys.stdin.readline().split()))
num_list = list(map(int, sys.stdin.readline().split()))

max_val = 0

def find_3_numbers():
    global max_val
    for i in range(0, len(num_list)-2): # 지옥의 3중 for 문
        for j in range(i+1, len(num_list)-1):
            for k in range(j+1, len(num_list)):
                current_sum = num_list[i] + num_list[j] + num_list[k]
                if current_sum < M:
                    max_val = max(max_val, current_sum)
                # if current_sum > M: # 더했을때 초과하는 경우
                #     pass
                # elif current_sum == M: # 더했을때 딱 맞는 경우
                #     return 0
                # else: # 더했을때 모자라는 경우
                #     min_val = min(min_val, abs(M-current_sum))

find_3_numbers()
print(max_val)

# 함수의 결과와 M 과의 차이를 나타내는 전역변수
# min_val = M



# 재귀함수 try
# def recursive(card_count, total, trail):
#     # print(total)
#     if card_count >= 3: # 재귀함수 탈출조건
#         return total
    
#     if total > M: # 약간의 시간단축을 위한
#         return False
    
#     global min_val

#     for num in num_list:
#         new_trail = trail[:]
#         new_trail.append(num)
#         current_return = recursive(card_count+1, total+num, new_trail)
#         print(current_return, new_trail)
#         if current_return != False:
#             min_val = min(min_val, abs(M-current_return))
#             if min_val == 0: # 약간의 시간단축을 위한 2
#                 return False
#     return total

# recursive(0,0, [])
# print(M-min_val)

# comb = list(combinations(num_list, 3))
# print(comb)


# 카드를 몇장 뽑았는지 count 해주는 변수
# card_count = 0

# 총 뽑은 카드를 더한 수
# answer = 0

# Descending order 로 sorting
# num_list.sort(reverse=True)


# 2. 큰 수부터 검사
# for num in num_list:
#     if M - num >= 0: # 현재 M 에서 뺴봐서 양수면 진행
#         print(num)
#         card_count += 1
#         answer += num
#         M -= num
#         if card_count == 3:
#             break

# print(answer)

