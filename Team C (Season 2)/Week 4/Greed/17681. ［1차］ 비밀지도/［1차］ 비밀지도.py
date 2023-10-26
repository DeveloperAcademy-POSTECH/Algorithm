def solution(n, arr1, arr2):
    answer = []
    for i in range(n):
        val = bin(arr1[i] | arr2[i])[2:]
        val = val.rjust(n,'0')
        tmp = val.replace("0"," ").replace("1","#")
        answer.append(tmp)
    return answer