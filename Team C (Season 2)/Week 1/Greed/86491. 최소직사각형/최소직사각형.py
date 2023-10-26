def solution(sizes):
    answer = 0
    maxW = 0
    maxH = 0
    
    for w,h in sizes:
        if h > w:
            w,h = h,w
        maxW = max(w,maxW)
        maxH = max(h,maxH)
        
    answer = maxW * maxH
    return answer