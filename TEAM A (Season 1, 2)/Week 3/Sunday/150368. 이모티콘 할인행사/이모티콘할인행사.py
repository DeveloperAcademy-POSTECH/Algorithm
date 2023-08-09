from itertools import product
def solution(users, emoticons):
    saledata = [10,20,30,40]
    중복순열할인데이터 = []
    answer = [0,0]
    # 우선 4의 7승의 조합을 만들자라고 생각을 하였다. => 중복순열
    for i in product(saledata, repeat = len(emoticons)):
        중복순열할인데이터.append(list(i))
    
    for j in 중복순열할인데이터 :
        num_subscribe = 0
        total_price = 0
        for user in users :
            salevalue, maxprice = user
            temp_price = 0
            for index, salepercent in enumerate(j):
                if(salevalue<=salepercent):
                    temp_price += (emoticons[index] * (100- salepercent) /100)
            if(temp_price >= maxprice):
                num_subscribe+=1
            else:
                total_price += temp_price
        if( answer[0] < num_subscribe):
            answer[0] = num_subscribe
            answer[1] = int(total_price)
        elif answer[0]==num_subscribe and answer[1] < total_price:
            answer[1]= int(total_price)
    return answer