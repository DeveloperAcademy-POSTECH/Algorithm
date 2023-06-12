# https://www.acmicpc.net/problem/2468
# 백준-2468-안전 영역

import sys

sys.setrecursionlimit(10**4)
input = sys.stdin.readline

def dfs(x, y, amount):
    if heights[y][x] <= amount:
        return 0
    heights[y][x] *= -1
    for idx in range(4):
        next_x, next_y = x + dx[idx], y + dy[idx]
        if 0 <= next_x < n and 0 <= next_y < n and heights[next_y][next_x] > amount:
            dfs(next_x, next_y, amount)
            
    return 1

def search(amount):
    safe_areas = 0
    for y in range(n):
        for x in range(n):
            safe_areas += dfs(x, y, amount)
    
    return safe_areas
    
n = int(input())
max_height = 0
heights = []
for _ in range(n):
    row = list(map(int, input().split()))
    max_height = max(max_height, max(row))
    heights.append(row)

dx = (0, 0, -1, 1)
dy = (-1, 1, 0, 0)

max_safe_areas = 1
for amount in range(1, max_height):
    heights = [[abs(height) for height in row] for row in heights]
    max_safe_areas = max(max_safe_areas, search(amount))
    
print(max_safe_areas)
'''
문제를 보고 떠올린 초기 아이디어는 다음과 같습니다.

1.
1) 강수량 값이 최대 높이와 같거나 그보다 크다면 모든 영역이 안전하지 않다. 안전 영역은 0개이다.
2) 강수량 값이 최대 높이보다 작다면 안전 영역이 적어도 1개 생긴다.
3) 강수량 값이 0일 때는 모든 영역이 안전하다. 안전 영역은 1개이다.

따라서 강수량 값을 0보다 크거나 같고, 최대 높이보다 작은 범위 내에서 변화시키면서 안전 영역의 개수를 센 다음 해당 개수를 안전 영역 최대 개수와 비교하며 갱신하면 되겠다고 생각했습니다.
높이는 1이상 100 이하의 정수이므로 최대 높이는 100이겠네요. 최악의 경우 강수량 값을 0~99 범위에서 변화시켜야 하므로 100번이 필요하겠습니다.

2.
다음으로는 안전 영역을 어떻게 세어볼 지 생각해야 합니다.
어떤 지점 (x,y)에 대해서 1)이 지점에 방문처리가 되어 있지 않고 2)해당 지점 높이값이 강수량 값보다 크다면 다음 지점을 탐색하게 하면 될 것 같다고 생각했습니다.
is_visited 변수에 Bool 값을 원소로 갖는 2차원 list를 할당해서 방문 여부를 판별하고자 했습니다. 
최악의 경우 100 * 100 = 10,000번을 탐색하게 됩니다. 

3.
따라서 상수배는 생략하고 100 * 10,000 = 1,000,000번 정도의 연산 횟수를 가질거라 판단했습니다. 시간 초과는 안 날 거라고 생각했습니다.

이러한 아이디어를 토대로 처음에 bfs를 시도했는데 메모리 초과가 났습니다.
is_visited를 따로 만들어서 방문을 체크하려 했는데 2차원 list heigths에서 이미 최대 10,000개의 값을 저장하는데 is_visited 또한 그만큼을 저장해야 하니 메모리 초과가 난 것 같았습니다.

해결 방법은 다음과 같습니다.

방문 처리는 필요한 작업이라 생각했기에 따로 2차원 배열을 생성하지 않고 어떻게 방문 여부를 판별할지 고민했습니다.
그러다 문득 새로운 지점을 탐색할 때 heights[y][x]를 통해 해당 지점의 높이가 물에 잠기는 지점인지 판별하는 부분을 이용해야겠다고 생각했습니다.

새로운 지점을 탐색할 때 그 지점을 안전 영역에 포함시키지 않는 경우는 다음과 같습니다.
1) 해당 지점의 높이가 물에 잠기는 높이일 경우 (heights[y][x] <= amount)
2) 해당 지점이 이미 안전 영역에 포함되어 있을 때(방문 처리가 되어 있을 때)

이 둘을 하나의 비교문으로 판별할 수 있게 하면 따로 2차원 배열을 생성하지 않고도 방문 여부를 판별할 수 있겠다 생각했습니다.
그래서 어떤 지점이 새롭게 안전 영역에 포함된다면 해당 지점의 높이값에 -1을 곱해 음수로 만들었습니다. 높이 값은 1 이상 100 이하의 값이므로 음수가 되면
반드시 강수량 값보다 작아지게 되기 때문이죠. 이를 통해 '높이가 모자라서 안전 영역이 될 수 없거나', '이미 방문한 지점이라 음수값을 가지거나' 둘의 경우를 heights[next_y][next_x] > amount 비교문 하나로 판별할 수 있게 했습니다.

이런 식으로 amount가 변경되어 새로운 강수량 값에 대해 안전 영역을 찾아야 할 경우에만 절대값을 이용해 높이값들을 초기화시켜주면서 안전 영역의 개수를 수집했고
그 중 최대값을 print하게 만들었습니다.
'''