from itertools import product

def solution(users, emoticons):
    dc_rate = [10, 20, 30, 40]
    possible_dc = product(dc_rate, repeat=len(emoticons))
    answer = [0, 0]
    for dc in possible_dc:
        member_count = 0
        sales = 0
        for user in users:
            threshold, limit = user
            temp_sales = 0
            for i in range(len(dc)):
                if dc[i] >= threshold:
                    temp_sales += emoticons[i] * 0.01 * (100 - dc[i])
                    
            if temp_sales >= limit:
                member_count += 1
            else:
                sales += temp_sales
                
        if member_count > answer[0]:
            answer = [member_count, sales]
        elif member_count == answer[0] and sales > answer[1]:
            answer = [member_count, sales]
            
    return answer
    