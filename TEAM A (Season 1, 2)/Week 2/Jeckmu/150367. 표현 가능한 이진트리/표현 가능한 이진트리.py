from collections import deque

def solution(numbers):
    answer = []
    for num in numbers:
        # num을 binary 2진수로 변환
        num = bin(num)[2:]
        n = 0
        # num의 자릿수가 2^(n-1) ~ (2^n)-1 사이에 있다는 것을 확인
        for i in range(10000):
            if len(num) < 2**i:
                n = i
                break

        # num의 자릿수가 (2^n)-1자리 꼴이 되도록 앞에 0을 추가
        while len(num) != 2**n-1:
            num = "0"+num

        # root node의 index.
        root = len(num)//2

        deq = deque([root])
        flag = True
        while n != 0 and flag:
            gap = 2**(n-2)
            if n == 1:
                break

            nextDeq = deque()
            while deq:
                a = deq.popleft()
                left = a - gap
                right = a + gap
                if num[a] == "0":
                    if num[left] == "1" or num[right] == "1":
                        answer.append(0)
                        flag = False
                        break

                nextDeq.append(left)
                nextDeq.append(right)

            deq = nextDeq
            n -= 1

        if flag == True:
            answer.append(1)
    return answer