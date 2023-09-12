import heapq

def solution(operations):
    heap = []
    
    for i in operations:
        operation, num = i.split(" ")
        num = int(num)
        if operation == 'I':
            heapq.heappush(heap, num)
        elif operation == 'D':
            if len(heap)==0:
                continue
            if num == 1:
                heap.remove(max(heap))
            elif num == -1:
                heapq.heappop(heap)
                
    if len(heap)==0:
        return [0,0]
    else:
        return [max(heap), heap[0]]
    