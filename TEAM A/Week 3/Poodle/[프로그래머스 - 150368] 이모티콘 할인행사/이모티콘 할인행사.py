from itertools import product

def solution(users, emoticons):
    answer = [0, 0]
    
    discounts_range = (10, 20, 30, 40)
    
    for discounts in product(discounts_range, repeat=len(emoticons)):
        current_purchases, current_sums = 0, 0
        
        for i in range(len(users)):
            user_discount_limit, user_purchase_limit = users[i]
            
            sums = 0
            for j in range(len(emoticons)):
                if discounts[j] >= user_discount_limit:
                    sums += emoticons[j] * ((100 - discounts[j]) / 100)
                    
            if sums >= user_purchase_limit:
                current_purchases += 1
            else:
                current_sums += sums
                
            if answer[0] < current_purchases or (answer[0] == current_purchases and answer[1] < current_sums):
                answer = [current_purchases, current_sums]

    return answer
