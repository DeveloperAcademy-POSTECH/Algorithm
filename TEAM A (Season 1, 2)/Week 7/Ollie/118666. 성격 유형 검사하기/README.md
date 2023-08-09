# [level 1] 성격 유형 검사하기 - 118666 

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/118666?language=python3) 

### 성능 요약

-

### 구분

코딩테스트 연습 > 2022 KAKAO TECH INTERNSHIP

### 채점결과

Empty

### 비고

예전에 풀었던 문제이나, 이전 풀이를 보지 않고 새롭게 풀어보았습니다.

### 문제 설명

#### Input
- survey
  - length: [1, 1K]
  - element:
    - 고정 길이 2인 String
    - 성격 유형
- choices
  - length: [1, 1K], survey와 동일한 길이
  - element
    - [1, 7] Int

#### Output
- 사용자의 성격 유형, 길이 4의 String

#### 방법
1. Key가 성격 유형, value가 유형 별 점수인 dictionary를 input을 순회하며 만든다.
2. 1의 dictionary를 활용하여 유형을 판단한다.

#### 이전 풀이와 달라진 점
- 파이썬의 list comprehension을 더 적극적으로 사용
- types라는 array를 만들었음.
  - dictionary는 원래 key에 순서가 보장되지 않는 자료구조이기 때문에.
  - 그런데 파이썬 3.7부터는 공식적으로 dictionary가 key의 순서를 기억한다.
    - https://blog.hwahae.co.kr/all/tech/6662
  - 이 차이를 알고 있는 한에서, 이전 풀이처럼 풀어도 무관할 것 같다.