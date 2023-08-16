# 11049 행렬 곱셈 순서
# https://www.acmicpc.net/problem/11049
# 2초
# 괄호를 적절히 쳐서 이 식의 값을 최소로 만들려고 함
# 0~9, +, - 로만 이루어져있음
# 식의 길이는 50보다 짧음

# 괄호 여러개 가능...미친넘...

# 도움받은 내용: 고차함수 flatten(), string method인 isdigit(), 최대 연속부분수열의 합

import sys

sys.stdin = open("1541_lostParenthesis/lostParenthesis.txt", "r")
input = sys.stdin

data = input.readline().split("-")

for i in range(len(data)):
    data[i] = sum(list(map(int, data[i].split("+"))))


answer = data[0]

for i in range(1,len(data)):
    answer -= data[i]


print(answer)

# for i in range(len(data)):
#     data[i] = eval(data[i])

# print(data[0] - sum(data[1:]))

# numbers = []
# operators = []

# number = ""
# for letter in data:
#     if letter == "+" or letter == "-":
#         operators.append(letter)
#         numbers.append(int(number))
#         number = ""

#     else:
#         number += letter
# numbers.append(int(number))

# minusPos = []
# for i in range(len(operators)):
#     if operators[i] == '-':
#         numbers[i+1] *= -1
#         minusPos.append(i+1)


# def getMaxSequence(arr):
#     arr[0] *= -1 # 첫번쨰 숫자에 붙은 음수는 괄호 밖의 음수니까
#     partialSum = 0
#     maxVal = -99999
#     maxIndex = 0

#     for i in range(len(arr)):
#         if partialSum + arr[i] >= arr[i]:
#             partialSum += arr[i]
#         else:
#             partialSum = arr[i]
        
#         if maxVal <= partialSum:
#             maxVal = partialSum
#             maxIndex = i
    
#     return (maxVal, maxIndex)

# maxVal = 0
# maxSequence = []
# startPos = 0
# endPos = 0

# for pos in minusPos:
#     arr = numbers[pos:]
#     result = getMaxSequence(arr)
#     if result[0] > maxVal:
#         maxVal = result[0]
#         startPos = pos
#         endPos = startPos + result[1]

# leftArr = numbers[:startPos]
# rightArr = numbers[endPos+1:]

# if len(minusPos) == 0:
#     print(sum(numbers))
# else:
#     print(sum(leftArr) + sum(rightArr) - maxVal)

