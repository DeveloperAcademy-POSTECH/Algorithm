def solution(arr):
    answer = [arr[0]]
    prev_item = arr[0]
    for i in range(1, len(arr)):
        if arr[i] != prev_item:
            answer.append(arr[i])
        prev_item = arr[i]
    return answer