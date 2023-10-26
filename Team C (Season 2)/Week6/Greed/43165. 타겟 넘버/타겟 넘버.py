def solution(numbers, target):
    answer = 0
    arr = [0]

    for num in numbers:
        tmp = []
        for result in arr:
            tmp.append(result + num)
            tmp.append(result - num)
        arr = tmp
    
    answer = arr.count(target)
    return answer