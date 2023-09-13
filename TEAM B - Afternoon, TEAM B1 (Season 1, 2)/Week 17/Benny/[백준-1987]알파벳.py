import sys

input = sys.stdin.readline

def dfs(x, y, count):
    temp_count = count
    for idx in range(4):
        next_x, next_y = x + dx[idx], y + dy[idx]
        if 0 <= next_x < c and 0 <= next_y < r and is_visited[ord(alphabets[next_y][next_x])-65] == False:
            is_visited[ord(alphabets[next_y][next_x])-65] = True
            temp_count = max(temp_count, dfs(next_x, next_y, count+1))
            is_visited[ord(alphabets[next_y][next_x])-65] = False
            
    return temp_count
            
r, c = map(int, input().split())
alphabets = []
for _ in range(r):
    alphabets.append(list(input().rstrip()))

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

is_visited = [False for _ in range(26)]
is_visited[ord(alphabets[0][0])-65] = True
        
#max_count = 1

print(dfs(0, 0, 1))

#print(max_count)