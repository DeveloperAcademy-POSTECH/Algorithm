# 1072 - 게임

# 게임 횟수 = X
# 이긴 게임 = Y
# 승률 = Z %
# (int(47/53 * 100)) = 88
# 승률이 변할때까지 최소 몇 판 더 해야 하는지, 절대 안변하면 -1
#

# 시간 초과
# import sys
# input = sys.stdin.readline
#
# X, Y = map(int, input().split())
# Z = int(Y/X * 100)
# winning = Z
# game = 0
#
# # 여기에 이진탐색 어떻게 쓴다는거지?
# while(winning == Z):
#     if(X==Y):
#         print(-1)
#         break
#     game += 1
#     X += 1
#     Y += 1
#     winning = int(Y/X * 100)
# else:
#     print(game)

#웨않되
import sys
input = sys.stdin.readline

X, Y = map(int, input().split())
# Z = int(Y/X * 100) # ->실수 연산의 부정확성!!
    # 29/50 = 0.58
    # 29/50*100 = 57.99999
# Z = int((Y * 100) / X)
Z = (Y*100)//X
if Z >= 99:# >= 99
    print(-1)
else:
    target = 1 # 0
    first = 0
    last = X # X-1 왜 아니지??!?!?
    while first <= last:
        mid = (first + last) // 2
        newX = X + mid
        newY = Y + mid
        if (newY * 100) // newX <= Z:
            first = mid + 1
        else:
            target = mid
            last = mid - 1
    print(target)
