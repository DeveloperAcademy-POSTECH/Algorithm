import sys
# from itertools import combinations

sys.stdin = open("2798_blackjack/blackjack.txt", "r")

N, M = list(map(int, sys.stdin.readline().split()))
num_list = list(map(int, sys.stdin.readline().split()))

min_val = M

def find_3_numbers():
    global min_val
    for i in range(0, len(num_list)-2): # 지옥의 3중 for 문
        for j in range(i+1, len(num_list)-1):
            for k in range(j+1, len(num_list)):
                current_sum = num_list[i] + num_list[j] + num_list[k]
                min_val = min(min_val, abs(M-current_sum))
                # if current_sum > M: # 더했을때 초과하는 경우
                #     pass
                # elif current_sum == M: # 더했을때 딱 맞는 경우
                #     return 0
                # else: # 더했을때 모자라는 경우
                #     min_val = min(min_val, abs(M-current_sum))

find_3_numbers()
print(M - min_val)