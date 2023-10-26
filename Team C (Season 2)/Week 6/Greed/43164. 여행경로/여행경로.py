import sys
sys.setrecursionlimit(10**6)

def solution(tickets):
    tickets.sort()
    visited = [0] * len(tickets)
    
    def dfs(start, path):
        path.append(start)

        if len(path) == len(tickets) + 1:
            return path

        for i in range(len(tickets)):
            if visited[i] == 0 and tickets[i][0] == start:
                visited[i] = 1
                
                result_path = dfs(tickets[i][1], path)
                
                if result_path: 
                    return result_path
                
                visited[i] = 0
                path.pop()
    
    answer = dfs("ICN", [])
    
    return answer