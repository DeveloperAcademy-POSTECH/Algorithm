def solution(progresses, speeds):
    answer = []
    
    while progresses: 
        count = 0
        progresses = [x+y for x,y in zip(progresses,speeds)]
        for i in progresses:
            if i < 100:
                break
            else:
                count += 1

        for i in range(count):
            progresses.pop(0)
            speeds.pop(0)  
                
        if count != 0:
            answer.append(count)        
    return answer