def solution(info, edges):
    global visited, answer
    visited = [False for _ in range(len(info))] 
    answer = []
    visited[0] = True
    def dfs(sheepnum, wolfnum):
        if sheepnum>wolfnum:
            answer.append(sheepnum)
        else: 
            return
        for parents, child in edges:
            if visited[parents] and not visited[child]:
                visited[child] = True
                if(info[child] == 0):
                    dfs(sheepnum+1,wolfnum)
                else:
                    dfs(sheepnum,wolfnum+1)
                visited[child] = False
    dfs(1,0)
    return max(answer)