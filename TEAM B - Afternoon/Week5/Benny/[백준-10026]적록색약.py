# https://www.acmicpc.net/problem/10026
# 백준-10026-적록색약

import sys
sys.setrecursionlimit(10**4) # 파이썬의 기본 재귀횟수제한은 1000번이라고 합니다. 문제에서 최대 10000번의 탐색을 해야 하므로 재귀횟수제한을 10000번으로 늘렸습니다.
# 대개 10**6 정도로 설정하면 된다고 합니다.
# 참고: https://help.acmicpc.net/judge/rte/RecursionError

input = sys.stdin.readline

def normal(colors, is_visited_normal, x, y):
    if is_visited_normal[y][x]:
        return 0
    else:
        is_visited_normal[y][x] = True
        for k in range(4):
            next_x, next_y = x + dx[k], y + dy[k]
            if 0 <= next_x < n and 0 <= next_y < n and colors[y][x] == colors[next_y][next_x]:
                normal(colors, is_visited_normal, next_x, next_y)   
        return 1
    
def weak(colors, is_visited_weak, x, y):
    if is_visited_weak[y][x]:
        return 0
    else:
        is_visited_weak[y][x] = True
        for k in range(4):
            next_x, next_y = x + dx[k], y + dy[k]
            if 0 <= next_x < n and 0 <= next_y < n:
                if colors[y][x] in 'RG' and colors[next_y][next_x] in 'RG':
                    weak(colors, is_visited_weak, next_x, next_y)
                elif colors[y][x] == 'B' and colors[next_y][next_x] == 'B':
                    weak(colors, is_visited_weak, next_x, next_y)
        return 1

n = int(input())
colors = []
for _ in range(n):
    colors.append(list(input().rstrip()))

is_visited_normal = [[False for _ in range(n)] for _ in range(n)]
is_visited_weak = [[False for _ in range(n)] for _ in range(n)]

# 상하좌우 순서로
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

count_normal = 0
count_weak = 0
for i in range(n):
    for j in range(n):
        count_normal += normal(colors, is_visited_normal, j, i)
        count_weak += weak(colors, is_visited_weak, j, i)
        
print(count_normal, count_weak)
'''
두 함수 'normal', 'weak'는 R과 G를 같은 색으로 여기느냐(weak) 그렇지 않느냐(normal)의 차이밖에 없습니다.
기본적으로 이미 방문한 위치라면 0을 return하고(구역을 count하기 위해서입니다), 한번도 방문한 적 없는 위치라면 이후의 작업을 수행하게 됩니다.
같은 색깔(혹은 같다고 여겨지는 색깔)의 경우에만 재귀적으로 다음 위치로 이동하게 됩니다. 더이상 이동할 곳이 없을 때 재귀가 끝이 나게 됩니다.

기본적으로 방문한 적이 없는 위치라면 1을 return하게 됩니다. 단 하나의 원소로 이루어진 구역도 있을 수 있기 때문입니다.

2중 for문을 통해 모든 원소를 순회합니다. 최대 10000번의 순회이므로 시간 제한에 걸리지 않습니다.
재귀적으로 알맞은 위치를 방문하고 해당 위치에 방문 표시를 합니다. 만약 2중 for문 첫번째(i=0, j=0)에서 재귀함수가 실행되어 i=0, j=1 위치에 방문 표시가 되었다면
그 이후 2중 for문에서 해당 위치를 찾아갔을 때 0이 return됩니다. 따라서 어떤 한 원소는 구역을 책정할 때 한번만 사용됩니다.
'''