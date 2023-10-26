from collections import deque

# deque 사용한 이중 반복문 (시간 초과)
def solution1(prices):
    prices_queue = deque(prices)
    answer = []
    count = 0
    
    while prices_queue:
        for i in range(len(prices_queue) - 1):
            if prices_queue[i] < prices_queue[0]:
                break
            count += 1
        prices_queue.popleft()
        answer.append(count)
        count = 0
    
    return answer


# 이중 for문
def solution2(prices):
    answer = []
    count = 0
    size = len(prices)
    
    for i in range(size - 1):
        for j in range(i + 1, size):
            count += 1
            if prices[i] > prices[j]:
                break
        answer.append(count)
        count = 0
    answer.append(0)

    return answer


# enumerate 사용한 이중 반복문
def solution3(prices):
    answer = []
    size = len(prices)
    
    for i, price in enumerate(prices):
        count = 0
        pos = i
        while pos < size and price <= prices[pos]:
            pos += 1
            if pos < size:
                count += 1
        answer.append(count)

    return answer


# enumerate 사용한 이중 for문
def solution4(prices):
    answer = []
    size = len(prices)
    
    for i, price in enumerate(prices):
        count = 0
        for j in range(i + 1, size):
            count += 1
            if price > prices[j]:
                break
        answer.append(count)

    return answer