import sys

input = sys.stdin.readline

def set_possiblity(n, row, column, possible):
    for i in range(n):
        if i != row:
            possible[i][column] += 1
            diff_row = abs(row-i)
            if 0 <= column-diff_row < n: 
                possible[i][column-diff_row] += 1
            if 0 <= column+diff_row < n: 
                possible[i][column+diff_row] += 1

def reset_possiblity(n, row, column, possible):
    for i in range(n):
        if i != row:
            possible[i][column] -= 1
            diff_row = abs(row-i)
            if 0 <= column-diff_row < n: 
                possible[i][column-diff_row] -= 1
            if 0 <= column+diff_row < n: 
                possible[i][column+diff_row] -= 1

def dfs(n, row):
    global count
    for column in range(n):
        if possible[row][column] == 0:
            set_possiblity(n, row, column, possible)
            if 0 <= row < n-1:
                dfs(n, row+1)
            else:
                count += 1
            reset_possiblity(n, row, column, possible)

n = int(input())
possible = [[0] * n for _ in range(n)]
count = 0

dfs(n, 0)
print(count)