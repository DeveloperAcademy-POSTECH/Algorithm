from collections import deque

def solution(begin, target, words):
    visited = [0] * len(words)
    queue = deque()
    queue.append(begin)

    while queue:
        cur_word = queue.popleft()
        
        for i,next_word in enumerate(words):
            if not visited[i]:
                cnt = sum(w1 != w2 for w1,w2 in zip(cur_word,next_word))
                if cnt == 1:
                    queue.append(next_word)
                    if cur_word == begin:
                        visited[i] = 1
                    else:
                        visited[i] += visited[words.index(cur_word)] + 1
                    if next_word == target:
                        return visited[i]

    return 0  