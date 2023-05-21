# 처음에는 10억이라는 N 의 자릿수를 보고 지레 쫄음
# 근데 알고보니 그냥 10개의 숫자를 정렬하는 문제였음
# 문제를 잘 읽어보자

import sys
sys.stdin = open("1427_sort_inside/sort_inside.txt","r")

# 아 이거 첼란이랑 베니한테 배운 코드 진짜 맘에 든다
num_list = list(str(int(sys.stdin.readline())))

num_list.sort(reverse=True)

# "구분자".join(lsit) -> 특정 리스트를 구분자를 사이에 넣은채로 합친다.
print("".join(num_list))