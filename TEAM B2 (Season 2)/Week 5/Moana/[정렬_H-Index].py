'''
테스트 케이스 11,, 왜 자꾸 실패하지
return cnt가 아니라 return i 여야했던 것임,,,,

'''

# def solution(citations):
#     for h in range(maxIndex,-1,-1): #0부터 최대 인용 횟수까지 돎
#         cnt = 0
#         for j in citations: 
#             if i <= j: 
#                 cnt += 1
#         if cnt <= i:
#             return i

#     return 0


def solution(citations):
    for h in range(len(citations),-1,-1):
        cnt = 0
        for cit in citations: 
            if h <= cit: 
                cnt += 1
        if cnt >= h:
            return h
        #return cnt 해서 틀렸음
    
    return 0