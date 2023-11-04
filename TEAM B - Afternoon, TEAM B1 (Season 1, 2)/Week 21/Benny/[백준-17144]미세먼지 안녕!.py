# https://www.acmicpc.net/problem/17144

import sys, copy

input = sys.stdin.readline

r, c, t = map(int, input().split())
room = []
cleaner = []
for i in range(r):
    temp = list(map(int, input().split()))
    if -1 in temp:
        cleaner.append((i, temp.index(-1)))
    room.append(temp)
    
dy, dx = [0, 1, 0, -1], [-1, 0, 1, 0]
def diffusion(x, y):
    if room2[y][x] == -1:
        return
    
    cur = room2[y][x]
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < c and 0 <= ny < r and room2[ny][nx] > -1:
            room[ny][nx] += cur // 5
            room[y][x] -= cur // 5
            
def cleanse():
    top, bottom = cleaner
    
    # 위쪽 청정기 순환
    if top[0] == 0:
        room[0] = [-1, 0] + room[0][1:-1]
    else:
        cx, cy = 0, top[0]-1
        while 0 < cy:
            room[cy][cx] = room[cy-1][cx]
            cy -= 1
        while cx < c-1:
            room[cy][cx] = room[cy][cx+1]
            cx += 1
        while cy < top[0]:
            room[cy][cx] = room[cy+1][cx]
            cy += 1
        while 1 < cx:
            room[cy][cx] = room[cy][cx-1]
            cx -= 1
        room[cy][cx] = 0
        
    # 아래쪽 청정기 순환
    if bottom[0] == r-1:
        room[r-1] = [-1, 0] + room[r-1][1:-1]
    else:
        cx, cy = 0, bottom[0]+1
        while cy < r-1:
            room[cy][cx] = room[cy+1][cx]
            cy += 1
        while cx < c-1:
            room[cy][cx] = room[cy][cx+1]
            cx += 1
        while bottom[0] < cy:
            room[cy][cx] = room[cy-1][cx]
            cy -= 1
        while 1 < cx:
            room[cy][cx] = room[cy][cx-1]
            cx -= 1
        room[cy][cx] = 0    
    
for _ in range(t):
    room2 = copy.deepcopy(room)
    for y in range(r):
        for x in range(c):
            diffusion(x, y)
 
    cleanse()

print(sum([sum(row) for row in room]) + 2)