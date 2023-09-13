def solution(n, arr1, arr2):
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
