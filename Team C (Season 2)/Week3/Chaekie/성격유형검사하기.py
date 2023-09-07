def solution(survey, choices):
    result = ''
    personality_type = {
        "R": 0, "T": 0, "C": 0, "F": 0, "J": 0, "M": 0, "A": 0, "N": 0
    }
    
    for answer, choice in zip(survey, choices):
        if choice == 1:
            personality_type[answer[0]] += 3
        elif choice == 2:
            personality_type[answer[0]] += 2
        elif choice == 3:
            personality_type[answer[0]] += 1
        elif choice == 5:
            personality_type[answer[1]] += 1
        elif choice == 6:
            personality_type[answer[1]] += 2
        elif choice == 7:
            personality_type[answer[1]] += 3
    
    type_list = list(personality_type.items())
    
    for i in range(0, len(type_list), 2):
        if type_list[i][1] >= type_list[i + 1][1]:
            result += type_list[i][0]
        else:
            result += type_list[i + 1][0]    

    return result


# zip, reverse slicing
# reversed() vs [::-1] -> reversed는 데이터 자체를 뒤집고 slicing은 데이터를 카피한 값을 
# 4(모르겠음, 0점)를 기준으로 양수 음수를 나눠 구분
def solution2(survey, choices):
    my_dict = {"RT": 0,"CF": 0,"JM": 0,"AN": 0}
    for A, B in zip(survey, choices):
        if A not in my_dict.keys():
            A = A[::-1]
            my_dict[A] -= B-4
        else:
            my_dict[A] += B-4

    result = ""
    for name in my_dict.keys():
        if my_dict[name] > 0:
            result += name[1]
        elif my_dict[name] < 0:
            result += name[0]
        else:
            result += sorted(name)[0]

    return result

print(solution2(["AN", "CF", "MJ", "RT", "NA"], [5, 3, 2, 7, 5]))