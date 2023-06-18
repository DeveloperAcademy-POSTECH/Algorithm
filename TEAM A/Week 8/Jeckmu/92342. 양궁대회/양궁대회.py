from itertools import product

def solution(n, info):
    A = list(product([True, False], repeat=11))

    max_score = 0
    max_list = [0,0,0,0,0,0,0,0,0,0,0]

    for a in A:
        num = n
        for i in range(11):
            if a[i]:
                num -= info[i]+1

        if num < 0:
            continue

        # 점수차 계산
        lion = 0
        apeach = 0
        for i in range(11):
            if a[i]:
                lion += 10-i
            elif info[i] > 0:
                apeach += 10-i

        if max_score < lion - apeach:
            max_score = lion - apeach
            temp = []
            for i in range(11):
                if a[i]:
                    temp.append(info[i]+1)
                else:
                    temp.append(0)

            temp[10] += num
            max_list = temp

        elif max_score == lion - apeach:
            temp = []
            for i in range(11):
                if a[i]:
                    temp.append(info[i]+1)
                else:
                    temp.append(0)

            temp[10] += num

            # 더 낮은 점수가 높다면 바꿔치기
            for i in range(10, -1, -1):
                if temp[i] > max_list[i]:
                    max_list = temp
                    break
                elif temp[i] < max_list[i]:
                    break

    if max_score == 0:
        max_list = [-1]
    
    return max_list