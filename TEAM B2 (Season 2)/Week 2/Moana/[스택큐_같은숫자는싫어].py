def solution(arr):
    answer = []
    tmp = arr[0]
    answer.append(tmp)
    for i in range(len(arr)):
        if arr[i] != tmp:
            answer.append(arr[i])
            tmp = arr[i]
    
    return answer