import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)   #무한 재귀호출을 방지

def dfs(x, y):
    # 주어진 범위를 벗어나는 경우인지 먼저 확인 - index 에러 방지
    if x < 0 or x >= n or y < 0 or y >= m:
        return False 
    if graph[x][y] == 1: #해당 노드가 0일때
        graph[x][y] = 0 #해당 노드를 먼저 방문 처리
        # 해당 노드의 상,하,좌,우의 위치도 모두 재귀적으로 호출
        dfs(x, y-1) #상
        dfs(x, y+1) #하
        dfs(x-1, y) #좌
        dfs(x+1, y) #우
        dfs(x-1, y+1)#대각선 상+좌
        dfs(x+1, y+1)#대각선 상+우
        dfs(x-1, y-1)#대각선 하+좌
        dfs(x+1, y-1)#대각선 하+우
        return True
    return False



while True :
    # 세로 길이 n, 가로 길이 m을 공백으로 구분하여 입력받기
    m, n = map(int, input().split()) # w가 먼저 오기 때문에 열 개수부터 받기.
    if n == 0 and m == 0 : #무한반복문의 종료조건
        break 
    # 2차원 리스트의 맵 정보 입력
    graph = []
    for _ in range(n):# 입력받은 수를 list 형태로 각 row에 append
        graph.append(list(map(int, input().split(' '))))

    # 얼음의 개수 (result)를 0으로 초기화
    result = 0

    for i in range(n):
        for j in range(m):
            if dfs(i,j) == True :
                result += 1

    print(result)