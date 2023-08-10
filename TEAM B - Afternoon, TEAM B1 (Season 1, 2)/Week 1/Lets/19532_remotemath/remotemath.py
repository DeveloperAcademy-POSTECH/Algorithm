# 2차 연립방정식을 푸는 문제
# ax + by = c
# dx + ey = f

# -> dax + dby = dc
# -> adx + aey = af
# 두개를 빼면, (db-ae)y = dc-af -> y = (dc-af) / (db-ae)

# -> eax + eby = ec
# -> bdx + bey = bf
# 두개를 빼면, (ea-bd)x = ec-bf -> x = (ec-bf) / (ea-bd)

# 역행렬로 해 구하는건 어떨까? -> 역행렬을 구할때 뭔가 double 이나 float 에서 오류날수도...
# 근데 어짜피 마지막에는 다 나눠주는데 오류 안나는거 보면 괜찮을지도?

import sys
sys.stdin = open("19532_remotemath/remotemath.txt", "r")

a, b, c, d, e, f = list(map(int, sys.stdin.readline().split()))

y = int((d*c - a*f) / (d*b - a*e))
x = int((e*c - b*f) / (e*a - b*d))

print(f"{x} {y}")

