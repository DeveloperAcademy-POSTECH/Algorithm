# 배열 arr 은 0부터 9까지
# 연속적으로 나타나는 숫자는 하나만 남기고 전부 제거
# 남은 수들을 반환할때는 원소의 순서는 유지

# 1,000,000 의 arr 길이
# 0 ~ 9 가 arr 내부

# 어떤 container 의 최상단에 있는거랑 같으면 안넣고 다르면 넣는 방법으로 하자

def solution(arr):
    answer = []
    answer.append(arr[0])
    

    for i in range(1, len(arr)):
        if arr[i] != answer[-1]:
            answer.append(arr[i])

    return answer

# # 뭔가 스택/큐니까 최대한 스택 큐 에서 어떻게 생각해볼지 고민함
# # 하나씩 돌면서 앞에 숫자랑 다르면 넣지 말자 -> stack 에서 최상단을 보는 원리

# def solution(arr):
#     # 일단 고정적으로 들어가는거니까 이거는 그냥 명시적으로 넣어줌
#     answer = [arr[0]]
    
#     # arr 의 index 1번부터 끝까지 돌면서, stack 의 최상단이랑 지속적으로 비교
#     for i in range(1, len(arr)):
#         if arr[i] != answer[-1]: # 만약 stack 의 최상단과 다르다? 그러면 stack 에 넣는다
#             answer.append(arr[i])
    

#     return answer
