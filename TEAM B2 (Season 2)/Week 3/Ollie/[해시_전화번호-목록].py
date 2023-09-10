
# 전화번호 목록
# https://school.programmers.co.kr/learn/courses/30/lessons/42577
from typing import List


def solution(phone_book: List[str]) -> bool:
    
    return True


# 1차 풀이, startswith를 사용한다 -> 시간초과 및 실패 
# ["119", "97674223", "1195524421"] 	false
def solution(phone_book: List[str]) -> bool:
    sorted_phone_book = sorted(phone_book, key=lambda x: (len(x), x[0]))
    answer = True
    
    for i, phone_number in enumerate(phone_book[:-1]):
        for other_phone_number in phone_book[i+1:]:
            if other_phone_number.startswith(phone_number):
                return False
    return answer



