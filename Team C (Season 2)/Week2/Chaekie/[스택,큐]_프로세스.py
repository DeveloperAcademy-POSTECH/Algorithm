from collections import deque 

def solution1(priorities, location):
    priorities_queue = deque(priorities)
    answer = 1
    
    while priorities_queue:
        if location == 0 and priorities_queue[0] == max(priorities_queue):
            return answer
        
        if priorities_queue[0] == max(priorities_queue):
            priorities_queue.popleft()
            answer += 1
        else:
            item = priorities_queue.popleft()
            priorities_queue.append(item)
            
        if location > 0:
            location -= 1
        else:
            location = len(priorities_queue) - 1 - location


# enumerate, any 활용한 풀이
## any() : 하나라도 True인게 있으면 True
## all() : 모두 True여야 True 반환
def solution2(priorities, location):
    queue =  [(i, v) for i, v in enumerate(priorities)]
    answer = 0
    print(queue)
    while True:
        cur = queue.pop(0)
        if any(cur[1] < prioritie[1] for prioritie in queue):
            queue.append(cur)
        else:
            answer += 1
            if cur[0] == location:
                return answer