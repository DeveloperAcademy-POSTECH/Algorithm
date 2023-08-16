# 각 기능은 진도가 100% 일때 서비스에 반영
# 각 기능의 개발속도가 모두 다르기때문에 뒤에 있는 기능이 앞에 있는 기능보다 먼저 개발 가능
# -> 만약 이렇다면 앞에 있는 기능이 완료되어야 뒤에 기능 같이 배포

# 배포 작업 순서 progresses
# 각 작업의 개발속도가 적힌 정수 배열 speeds

# 각 배포마다 몇 개의 기능이 배포되는지 return

# 1. deque 에 progresses 와 speeds 를 둘 다 넣고
# 2. progresses 의 가장 처음이 100 을 넘으면, progresses 와 speeds 둘 다 pop
# 3. 2의 과정을 while 문을 통해 100 이 넘는걸 한번에 pop 해주기

from collections import deque # deque 를 import

def solution(progresses, speeds):
    answer = []
    dq_progress = deque(progresses) # 각 list 를 deque 로 변경
    dq_speeds = deque(speeds)
    
    while len(dq_progress) != 0: # 작업이 다 deque 에서 빠져나갈때까지 반복
        # print(dq_progress)
        for i in range(len(dq_progress)): # 각 작업의 당일 진도를 더해줌
            dq_progress[i] += dq_speeds[i]
        
        pop_cnt = 0 # 몇개 pop 했는지 count
        while dq_progress[0] >= 100: # progress 의 맨 앞부터 100을 넘긴 모든 작업을 뺴줌
            dq_progress.popleft()
            dq_speeds.popleft()
            pop_cnt += 1
            if len(dq_progress) == 0:
                break
        
        if pop_cnt > 0:
            answer.append(pop_cnt) # 마지막으로 그날 배포 pop 한 작업의 갯수를 answer 에 더해줌

    return answer


