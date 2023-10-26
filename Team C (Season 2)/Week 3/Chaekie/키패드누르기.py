def solution1(numbers, hand):
    answer = ''
    keypad = {1: (0, 0), 2: (0, 1), 3: (0, 2),
              4: (1, 0), 5: (1, 1), 6: (1, 2),
              7: (2, 0), 8: (2, 1), 9: (2, 2),
              "*": (3, 0), 0: (3, 1), "#": (3, 2)}
    left_position = keypad["*"]
    right_position = keypad["#"]
    
    for number in numbers:
        if number in [1, 4, 7]:
            answer += "L"
            left_position = keypad[number]
        elif number in [3, 6, 9]:
            answer += "R"
            right_position = keypad[number] 
        else:
            tmp_position = keypad[number]
            left_distance = abs(left_position[0] - tmp_position[0]) + abs(left_position[1] - tmp_position[1])
            right_distance = abs(right_position[0] - tmp_position[0]) + abs(right_position[1] - tmp_position[1])
            
            if left_distance < right_distance or (left_distance == right_distance and hand == "left"):
                answer += "L"
                left_position = keypad[number]
            else:
                answer += "R"
                right_position = keypad[number]
        
    return answer

