# https://www.acmicpc.net/problem/21608
# 백준-21608-상어 초등학교

import sys

input = sys.stdin.readline

def set_position(student):
    global board
    global infos
    
    storage = [[] for _ in range(15)]
    for i in range(n):
        for j in range(n):
            like_count = 0
            empty_count = 0

            for k in range(4):
                nj = j + dj[k]
                ni = i + di[k]
                if 0 <= nj < n and 0 <= ni < n:
                    if board[ni][nj] in infos[student]:
                        like_count += 1
                    if board[ni][nj] == 0:
                        empty_count += 1
         
            storage_idx = 0
            for k in range(like_count):
                storage_idx += 5 - k

            storage_idx += empty_count
            if board[i][j] == 0:
                storage[storage_idx].append([i, j])

    for k in range(14, -1, -1):
        if storage[k] != []:
            i, j = storage[k][0]
            board[i][j] = student
            break
            
def check_like(i, j):
    like_count = 0
    for k in range(4):
        nj = j + dj[k]
        ni = i + di[k]
        if 0 <= nj < n and 0 <= ni < n:
            if board[ni][nj] in infos[board[i][j]]:
                like_count += 1
                
    return 0 if like_count == 0 else 10 ** (like_count - 1)

n = int(input())
infos = {}
for _ in range(n**2):
    student, a, b, c, d = map(int, input().split())
    infos[student] = [a, b, c, d]
    
board = [[0] * n for _ in range(n)]

dj = [0, 1, 0, -1]
di = [-1, 0, 1, 0]

for student in infos.keys():
    set_position(student)
    
satisfaction = 0
for i in range(n):
    for j in range(n):
        satisfaction += check_like(i, j)
        
print(satisfaction)