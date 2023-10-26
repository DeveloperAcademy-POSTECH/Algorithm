def solution1(n, arr1, arr2):
    answer = []
    arr1 = [format(item, 'b') for item in arr1]
    arr2 = [format(item, 'b') for item in arr2]
    n = 0
    
    for item1, item2 in zip(arr1, arr2):
        n = max(n, len(item1), len(item2))

    for item1, item2 in zip(arr1, arr2):
        if len(item1) < n:   
            item1 = (n - len(item1))* '0' + str(item1)
        if len(item2) < n:
            item2 = (n - len(item2))* '0' + str(item2)

        result = ""
        for i1, i2 in zip(item1, item2):
            if int(i1) | int(i2):
                result += "#"
            else:
                result += " "
        answer.append(result)
              
    return answer


# rjust 사용해서 앞에 0 채워주기
# replace 연속 사용 가능
def solution2(n, arr1, arr2):
    answer = []
    for item1, item2 in zip(arr1, arr2):
        a12 = str(bin(item1 | item2)[2:])
        a12 = a12.rjust(n,'0')
        a12 = a12.replace('1','#').replace('0',' ')
        answer.append(a12)
    return answer
