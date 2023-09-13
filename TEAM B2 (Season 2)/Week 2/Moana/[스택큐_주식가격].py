def solution(prices):
    answer = []
    price = 0
    size = len(prices)
    
    for j in range(size-1):
        for k in range(j+1, size):
            if prices[j] <= prices[k]:
                price += 1
            else:
                price += 1
                break
        answer.append(price)
        price = 0
    answer.append(0)

    return answer