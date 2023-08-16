from collections import defaultdict
from heapq import heappush, heappop

edges = defaultdict(dict)

def solution(n, paths, gates, summits):
    # 간선 초기화
    for i, j, w in paths:
        edges[i][j] = w
        edges[j][i] = w
    
    is_summit = [False for _ in range(n + 1)]
    for idx in summits: is_summit[idx] = True

    # 다익스트라를 위한 초기화
    intensity = [1e9 for _ in range(n + 1)]
    q = []

    # 다익스트라 시작 지점 설정
    for gate in gates:
        heappush(q, (0, gate))
        intensity[gate] = 0

    # 다익스트라 수행
    while q:
        current_intensity, current = heappop(q)
        # print(current_intensity, current)
        
        # 이미 구한 경로가 더 최단거리이거나, 정상에 도달한 경우 continue
        if intensity[current] < current_intensity or is_summit[current]:
            continue

        for neighbor in edges[current].keys():
            # 기존 다익스트라에서 변형된 부분
            next_intensity = max(intensity[current], edges[current][neighbor])

            if intensity[neighbor] > next_intensity:
                intensity[neighbor] = next_intensity
                heappush(q, (next_intensity, neighbor))

    answer = [-1, 1e9]

    for summit in summits:
        if intensity[summit] < answer[1] or (intensity[summit] == answer[1] and summit < answer[0]):
            answer = [summit, intensity[summit]]
    
    return answer
