def solution(phone_book):
    phone_book.sort()
    answer = True
    
    for i in range(len(phone_book)-1):
        # if phone_book[i] in phone_book[i+1]:
#         포함이 아니라 '접두어'여야함
        if phone_book[i] == phone_book[i+1][:len(phone_book[i])]:
            answer = False
            break
    return answer