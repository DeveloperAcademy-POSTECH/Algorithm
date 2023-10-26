def solution(numbers, hand):
    pad = {'1':(0,0), '2':(0,1), '3':(0,2),
           '4':(1,0), '5':(1,1), '6':(1,2),
           '7':(2,0), '8':(2,1), '9':(2,2),
           '*':(3,0), '0':(3,1), '#':(3,2)
        }
    answer = ''
    hand = "R" if hand == "right" else "L"
    leftPos = pad['*']
    rightPos = pad['#']
    for i in numbers:
        if i in [1,4,7]:
            answer += "L"
            leftPos = pad[str(i)]
        elif i in [3,6,9]:
            answer += "R"
            rightPos = pad[str(i)]
        else: # 2,5,8,0 일때
            #번호와 왼손의 거리 계산
            left_dis = abs(leftPos[0] - pad[str(i)][0]) + abs(leftPos[1] - pad[str(i)][1])
            #번호와 오른손의 거리 계산
            right_dis = abs(rightPos[0] - pad[str(i)][0]) + abs(rightPos[1] - pad[str(i)][1])
            if left_dis > right_dis:
                answer += "R"
                rightPos = pad[str(i)]
            elif left_dis < right_dis:
                answer += "L"
                leftPos = pad[str(i)]
            else:
                answer += hand
                if hand == "R":
                    rightPos = pad[str(i)]
                else:
                    leftPos = pad[str(i)]
    return answer
