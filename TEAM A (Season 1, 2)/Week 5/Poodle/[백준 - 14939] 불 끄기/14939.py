# 백준 14939번: 불 끄기

from itertools import product
import sys

input = sys.stdin.readline

original_lights = [list(input().rstrip()) for _ in range(10)]

turn = []
light_state = [True, False]
toggle = {"#": "O", "O": "#"}

directions = ((0, 1), (0, -1), (1, 0), (-1, 0))

def all_off(lights):
    for r in range(8, 10):
        for c in range(10):
            if lights[r][c] == 'O':
                return False
    return True

answer = int(1e9)

# 첫 번째 줄을 클릭하는 경우의 수 2^10 = 1024 ~= 10^3
for first_line in product(light_state, repeat=10):
    lights = [['#' for _ in range(10)] for _ in range(10)]
    for r in range(10):
        for c in range(10):
            if original_lights[r][c] == 'O': lights[r][c] = 'O'

    cnt = 0

    # 첫 번째 줄의 스위치를 일괄 조작
    for idx in range(len(lights)):
        if first_line[idx]: 
            lights[0][idx] = toggle[lights[0][idx]]
            cnt += 1
            for dr, dc in directions:
                if 0 <= dr < 10 and 0 <= idx + dc < 10:
                    lights[dr][idx + dc] = toggle[lights[dr][idx + dc]]

    # 두 번째 줄 ~ 마지막 줄까지 아래로 내려가면서 조작
    for r in range(1, 10):
        for c in range(10):
            # 자신의 윗 칸 전구가 켜져 있으면
            if lights[r - 1][c] == 'O':
                # 해당하는 스위치를 토글
                lights[r][c] = toggle[lights[r][c]]
                cnt += 1
                for dr, dc in directions:
                    if 0 <= r + dr < 10 and 0 <= c + dc < 10:
                        lights[r + dr][c + dc] = toggle[lights[r + dr][c + dc]]
        
        # for row in lights:
        #     print(*row)
        # print()

    if all_off(lights):
        answer = min(answer, cnt)

print(answer if answer < int(1e9) else -1)
