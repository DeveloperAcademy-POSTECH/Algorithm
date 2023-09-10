def solution(nums):
    tmpnum = max(nums)+1
    pocketmonList = [0 for i in range(tmpnum)]
    answer = 0
    
    for i in nums:
        pocketmonList[i] += 1
        
    for i in pocketmonList:
        if i != 0:
            answer += 1
        if answer >= len(nums)/2:
            break
    
    return answer