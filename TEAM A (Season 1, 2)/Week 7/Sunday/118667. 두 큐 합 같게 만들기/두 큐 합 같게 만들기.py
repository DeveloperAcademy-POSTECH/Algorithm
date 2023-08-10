from collections import deque
def solution(queue1, queue2):
    answer = 0
    maxnum = len(queue1)
    deque1 = deque(queue1)
    deque2 = deque(queue2)
    sum1 = sum(queue1)
    sum2 = sum(queue2)
    if((sum1 + sum2) %2 == 1):
        return -1 
    while True : 
        if(sum1>sum2):
            a = deque1.popleft()
            deque2.append(a)
            sum1-=a
            sum2+=a
        elif(sum1<sum2):
            b= deque2.popleft()
            deque1.append(b)
            sum1+=b
            sum2-=b
        else:   
            return answer
        answer += 1
        if answer == maxnum * 3 : 
            return -1
    return answer