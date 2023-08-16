# 숫자 카드 N 개
# 정수가 M 개 주어졌을 때, 상근이가 이 숫자들 중 몇개를 갖고 있는지 구하기

# N <= 500,000, M <= 500,000
# nlogn 안으로 끊어야겠넹
# 흠.... 어캐 해야할까나...
# 처음 든 생각은 그냥 둘 다 sort 하고 찾는게 빠를것 같은데
# 아니면 dict 로 hash 를 이용해서 찾거나


import sys
sys.stdin = open("10816_numberCard2/numberCard2.txt", "r")

N = sys.stdin.readline() # 갖고 있는 N 개의 카드를 입력받음
have_card = list(map(int, sys.stdin.readline().split()))

M = sys.stdin.readline() # 찾아야할 M 개의 카드를 입력받음
given_card = list(map(int, sys.stdin.readline().split()))

number_dict = {} # hashing 을 위한 dict 생성
for i in range(len(have_card)): # dict 에 정수마다 몇개의 카드를 갖고 있는지 넣기
    if number_dict.get(have_card[i]) == None:
        number_dict[have_card[i]] = 1
    else:
        number_dict[have_card[i]] += 1

answer = []
for i in range(len(given_card)): # 마지막으로 M 개의 카드가 각각 몇개 있는지 찾기
    temp = number_dict.get(given_card[i])
    if temp == None:
        answer.append("0")
    else:
        answer.append(str(temp))


print(" ".join(answer))
