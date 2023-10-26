def solution(brown, yellow):
    t = int((brown - 4)/2)
    
    for i in range(2 * t):
        width = t - i
        height = t - width
        if width * height == yellow and width >= height:
            answer = [width + 2, height + 2]
            
    return answer