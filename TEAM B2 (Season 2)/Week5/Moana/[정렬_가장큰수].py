def solution(numbers):
    numbers = list(map(str, numbers))
    #원소가 0이상 1,000이하이므로 4배하고 4자리만 비교하면 됨
    #문자열이라 사전순서대로 정렬이 됨
    numbers.sort(key=lambda x: (x*4)[:4], reverse=True)

    return ''.join(numbers) if ''.join(numbers)[0] != '0' else '0'
