from itertools import permutations

# 영수가 대답한 횟수
round = int(input())

# 나올 수 있는 숫자 조합 생성
numSet = list(permutations((1, 2, 3, 4, 5, 6, 7, 8, 9), 3))  

# 입력값을 numSet의 조합들과 일일이 대조
for _ in range(round):
    # 대조할 민혁이의 값, 스트라이크 개수, 볼 개수 변수에 할당
    minheok, strike, ball = map(int, input().split())
    minheok = list(str(minheok))
    removeCount = 0

    # numSet 숫자 조합 돌리기
    for i in range(len(numSet)):
        strikeCount = ballCount = 0
        i -= removeCount

        # 민혁이의 값이 대조값에 존재하는 경우, 
        # 민혁이의 값의 위치가 대조값과 같다면 strikeCount + 1, 같지 않다면 ballCount + 1
        for j in range(3):
            minheok[j] = int(minheok[j])

            if minheok[j] in numSet[i]:
                if j == numSet[i].index(minheok[j]):
                    strikeCount += 1
                else:
                    ballCount += 1
        
        # 대조 후 strikeCount, ballCount이 기존 strike, ball과 일치하지 않으면 선택지에서 제외 (현재 대조값을 리스트에서 제거)
        if strikeCount != strike or ballCount != ball:
            numSet.remove(numSet[i])
            # 리스트에서 제거된 대조값 개수 증가
            removeCount += 1

# 숫자 조합에서 제거되고 남은 선택지 개수
print(len(numSet))



