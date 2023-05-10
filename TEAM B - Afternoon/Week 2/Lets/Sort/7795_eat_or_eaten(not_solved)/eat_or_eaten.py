# A 가 B 를 먹음
# A 는 자기보다 크기가 작은 B 만 먹을 수 있음
# 먹을 수 있는 순서쌍을 구하는 문제
# 시간제한 1초
# A 와 B 의 갯수는 20000 -> nlongn 까지는 괜찮을듯?

import sys
sys.stdin = open("7795_eat_or_eaten/eat_or_eaten.txt", "r")

tc = int(sys.stdin.readline())

for t in (1, tc+1):
    N, M = list(map(int, sys.stdin.readline().split()))

    A = list(map(int, sys.stdin.readline().split()))
    B = list(map(int, sys.stdin.readline().split()))

    # A.sort()
    # B.sort()

    # print(A)
    # print(B)

    set_A = set(A)
    set_B = set(B)
    final_A = list(set_A)
    final_B = list(set_B)
    final_A.sort()
    final_B.sort()

    # print(final_A)
    # print(final_B)

    cnt = 0

    for a in final_A:
        for b in final_B:
            if a > b:
                print(f"{a}-{b}")
                cnt += 1
            else:
                break
    # for a in A:
    #     for b in B:
    #         if a > b:
    #             print(f"{a}-{b}")
    #             cnt += 1
    #         else:
    #             break

    print(cnt)