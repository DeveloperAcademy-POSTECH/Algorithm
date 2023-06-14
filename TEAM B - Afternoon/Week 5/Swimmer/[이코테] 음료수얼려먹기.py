# 세로 길이 n, 가로 길이 m을 공백으로 구분하여 입력받기
n, m = map(int, input().split())

# 2차원 리스트의 맵 정보 입력
graph = []
for _ in range(n):# 입력받은 수를 list 형태로 각 row에 append
    graph.append(list(map(int, input().split(' ')))) 

def dfs(x, y):
    # 주어진 범위를 벗어나는 경우인지 먼저 확인 - index 에러 방지
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False 
    if graph[x][y] == 0: #해당 노드가 0일때
        graph[x][y] = 1 #해당 노드를 먼저 방문 처리
        # 해당 노드의 상,하,좌,우의 위치도 모두 재귀적으로 호출
        dfs(y-1,x) #상
        dfs(y+1,x) #하
        dfs(y,x-1) #좌
        dfs(y,x+1) #우
        return True
    return False

# 얼음의 개수 (result)를 0으로 초기화
result = 0

for i in range(n):
    for j in range(m):
        if dfs(i,j) == True :
            result += 1

print("결과는"+str(result))