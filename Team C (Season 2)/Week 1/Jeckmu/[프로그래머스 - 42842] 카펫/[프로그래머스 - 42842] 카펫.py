from math import sqrt
def solution(brown, yellow):
    answer = []

    # yellow�� m x n ����̸�
    # ��ü�� (m+2) x (n+2) ����̰�
    # brown�� 2m + 2n + 4 �� (mn+2(m+n)+4-mn = 2m+2n+4)

    for i in range(1, int(sqrt(yellow))+1):
        if yellow % i == 0:
            if 2*i + 2*int(yellow/i) + 4 == brown:
                answer = [int(yellow/i)+2, i+2]
                
    return answer