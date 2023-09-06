
# 이중우선순위큐
# https://school.programmers.co.kr/learn/courses/30/lessons/42628
from typing import List
import heapq

del_min_op = "D -1"
del_max_op = "D 1"

def solution(operations: List[str]) -> List[int]:
    hq = []
    is_hq_reversed = False
    for operation in operations:
        if operation == del_min_op:
            if not hq: continue
            # delete min
            if is_hq_reversed:
                hq = [ x * -1 for x in hq ]
                is_hq_reversed = not is_hq_reversed
                heapq.heapify(hq)
            heapq.heappop(hq)
        elif operation == del_max_op:
            if not hq: continue
            # delete max
            if not is_hq_reversed:
                hq = list(map(lambda x: x*-1, hq))
                is_hq_reversed = not is_hq_reversed
                heapq.heapify(hq)
            heapq.heappop(hq)
        else:
            # insert
            parsed_int = int(operation[2:]) * -1 if is_hq_reversed else int(operation[2:])
            heapq.heappush(hq, parsed_int)
    
    if not hq: return [0, 0]

    sorted_hq = sorted(hq)
    
    answer = [sorted_hq[-1], sorted_hq[0]] if not is_hq_reversed else [sorted_hq[0], sorted_hq[-1]]
    return answer


if __name__ == "__main__":
    opers = ["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]
    sol = solution(operations=opers)
    print(sol)