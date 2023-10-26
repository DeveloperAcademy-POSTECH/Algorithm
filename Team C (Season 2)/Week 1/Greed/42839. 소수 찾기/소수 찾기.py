import itertools

def solution(numbers):
    arr = []
    answer = 0
    number = list(numbers)
    for i in range(len(number)):
        for j in itertools.permutations(number, i+1):
            arr.append(int(''.join(j))) 
    num_list = list(set(arr))
    print(num_list)
    # 소수 찾기
    for i in num_list:
        if i <= 1:
            continue
        tmp = 0
        for j in range(2,int(i**0.5)+1):
            if i % j == 0:
                tmp += 1
        if tmp >= 1:
            continue
        else:
            answer += 1
    return answer