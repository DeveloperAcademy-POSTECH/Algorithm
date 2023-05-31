# priorities 는 각 자리의 priorities 를 알려줌
# location 에 해당하는 작업이 몇번째에 뽑히는지 return

# 일단 queue 형태로 돌아가야하니까 deque 를 쓰자

from collections import deque

def solution(priorities, location):
    
    dq = deque() # deque 생성 # 여기에는 target 인지 아닌지와, priority 를 묶어서 넣어줌
    
    # dq = [(priority1, target)...] 이런 형태로 만듬
    for i in range(len(priorities)):
        if i == location:
            dq.append((priorities[i], True))
        else:
            dq.append((priorities[i], False))
    
    # 전체 연산을 하는 high_priority 함수
    return high_priority(dq)


def high_priority(dq):
    cnt_value = 0 # 총 몇개의 process 가 실행되었는지 갯수를 세는 변수
    
    highest_priority = max(dq)[0] # deque 의 가장 높은 priority 를 세팅
    
    while len(dq) != 0: # 내가 원하는 process 가 pop 될 때 까지 도는 while 문
        cur_process = dq.popleft()
        # highest_priority = max(dq)[0] # 다시 highest priority 를 재설정
        if cur_process[0] == highest_priority: # 가장 priority 가 높은 녀석을 뽑았을때
            cnt_value += 1 # process 진행했다는 cnt 를 늘림
            
            if len(dq) != 0:
                highest_priority = max(dq)[0] # 다시 highest priority 를 재설정
            
            if cur_process[1] == True: # 만약 찾던 process 라면
                return cnt_value # 현재까지의 cnt value 를 반환
        else:
            dq.append(cur_process)

# def solution(priorities, location):
#     answer = 0
#     # 인쇄 대기목록의 가장 앞에 있는 문서를 꺼냄
#     # 나머지 인쇄 대기목록에서 맨 앞보다 중요한 대기목록이 있으면 맨앞을 맨 뒤로
#     # 그렇지 않으면 맨 앞을 인쇄

#     # priorities: 인쇄 대기 큐
#     # location: 내가 인쇄를 요청한 문서가 현재 어디에 있는지
#     # 숫자가 클 수록 중요

#     # 각 페이지를 마킹하기 위해서 2차원배열을 만듬
#     print_q = [[priorities[i], chr(i + ord('A'))] for i in range(len(priorities))]

#     # 내가 뽑고 싶은 페이지
#     my_page = print_q[location][1]


#     count = 1
#     while print_q != []:
#         # 맨 앞에 있는게
#         # max값인지 확인
#         if print_q[0][0] == max(print_q)[0]:
#             # max이면서 내 page면 return
#             if print_q[0][1] == my_page:
#                 return count
#             # max인데 내꺼가 아님 그러면 count 1증가
#             else:
#                 print_q.pop(0)
#                 count += 1
#         # max값이 아님
#         # 그러면 다시 큐의 뒤에다가 넣음
#         else:
#             printed = print_q.pop(0)
#             print_q.append(printed)

#     return answer