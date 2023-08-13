def solution(n, info):
    answer = [-1]
    max_win_score = 0
    min_hit = 0
    
    # print(info)
    # print("-----------------")
    
    # 쏘는 화살의 수 N <= 10
    # 어떤 점수에 어피치보다 많이 맞추지 않는다면 그 점수에 쏘는 화살은 무의미해짐
    # 그리디 전략: 어떤 점수에 어피치 + 1만큼 쏘거나, 아니면 아예 안 쏠 수 있음
    
    def bruteforcing(current_answer, score, remains, current_min_hit, idx):
        nonlocal answer, max_win_score, min_hit
        
        # print(f"bruteforcing({current_answer}, {score}, {remains}, {idx})")
        
        if idx > 10:
            if score > max_win_score or (score == max_win_score and current_min_hit < min_hit):
                answer = current_answer.copy()
                max_win_score = score
                min_hit = current_min_hit
            # print(current_answer, score)
            return
        
        elif idx == 10:
            current_answer[idx] = remains

            if remains >= info[idx] + 1:
                bruteforcing(current_answer, score + (10 - idx), 0, 10 - idx, idx + 1)
            else:
                if info[idx] == 0:
                    bruteforcing(current_answer, score, 0, current_min_hit, idx + 1)
                else:
                    bruteforcing(current_answer, score - (10 - idx), 0, current_min_hit, idx + 1)
        else:
            if remains >= info[idx] + 1:
                current_answer[idx] = info[idx] + 1
                bruteforcing(current_answer, score + (10 - idx), remains - (info[idx] + 1), 10 - idx, idx + 1)

            current_answer[idx] = 0
            if info[idx] == 0:
                bruteforcing(current_answer, score, remains, current_min_hit, idx + 1)
            else:
                bruteforcing(current_answer, score - (10 - idx), remains, current_min_hit, idx + 1)
            
    bruteforcing([0] * 11, 0, n, 11, 0)
    
    return answer
