# 프로세스
# https://school.programmers.co.kr/learn/courses/30/lessons/42587


def solution(priorities, location):
    pass


from collections import deque
from collections import Counter

def solution(priorities, location):
    answer = 0
    p_cnt = Counter(priorities)
    q = deque([(p, i) for i,p in enumerate(priorities)])
    curr_max = max(p_cnt)
    num_max = p_cnt[curr_max]
    while q:
        c_pri, c_idx = q.popleft()
        if c_pri == curr_max:
            answer += 1
            num_max -= 1
            if location == c_idx:
                return answer
            if num_max == 0:
                del p_cnt[curr_max]
                curr_max = max(p_cnt)
                num_max = p_cnt[curr_max]
        else:
            q.append((c_pri, c_idx))
    return answer