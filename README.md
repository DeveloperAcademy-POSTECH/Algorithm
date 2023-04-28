# Algorithm Study 

#### in Apple Developer Academy @ POSTECH

<br />

## ⏰ Time & Period

- 기간 : 4월 4째주 ~ 6월 4째주 (10주)
- Meeting
  - TEAM A - 월요일 12:40pm (오후 세션 이전)
  - TEAM B (Morning) - 금요일 12:40pm (오후 세션 이전)
  - TEAM B (Afternoon) - 수요일 6:00pm (오후 세션 이후)

<br />

## Participants

- TEAM A
  - 🚩🚩 [Jeckmu / 이재원](https://github.com/220v-K)
  - [Ollie / 김세이](https://github.com/vanism2091)
  - [Eren / 문희찬](https://github.com/mun9769)
  - [Woody / 박현우](https://github.com/migusdn)
  - [Sunday / 이선호](https://github.com/Sunhofficial)
  - [Poodle / 최어진](https://github.com/poodlepoodle)
- TEAM B - Morning
  - 🚩 [Shannon / 이세민](https://github.com/cutthebutter)
  - [Ddan / 박승찬](https://github.com/eemdeeks)
  - [Jerry / 이주환](https://github.com/jhwan2)
  - [Cyndi / 박지은](https://github.com/cyndi0330)
  - [Lianne / 최예은](https://github.com/lianne-b)
  - [Hayo / 김동혁]()
- TEAM B - Afternoon
  - 🚩 [Swimmer / 황지우](https://github.com/earlysummer0303)
  - [Lets / 고석환](https://github.com/alpaka99)
  - [Soda / 김민](https://github.com/minnnidev)
  - [Celan / 이승준](https://github.com/valselee)
  - [Benny / 한기백](https://github.com/ivorrr987)
  - [Madeline / 신정연](https://github.com/MADElinessss)

<br />

## Process

### TEAM A

- 주마다 풀 문제를 정합니다.

- 미팅날 까지 풀어옵니다!
- 미팅날 사다리타기🪜로 발표할 문제를 정합니다.

- `for problem in problems_this_week:`
  - 담당한 사람이 문제에 대해 발표합니다. 
    - Ex. 문제에 대한 초견, 생각한 접근법, 실패 과정, 코드 개선 과정, 결과. Time Complexity / Space Complexity 분석. 후기.. etc.
  - 문제에 대한 각자의 후기를 남깁니다.
    - Ex. 이거 이렇게 풀면 더 깔끔해요! / 이거 Time Complexity가 이게 아니라 저렇게 되는 것 같습니당. / 이 문제 너무 어려웠음 ㅠㅠ

### TEAM B (Morning / Afternoon)

- 매 주 공부할(문제를 풀) 주제를 정합니다. (Ex. Stack, Queue, Greedy, Dynamic Programming..)
- 각자 자신에게 맞는 난이도의 문제를 5문제가량 미팅날까지 풀어옵니다!
- `for person in TEAM:`
  - 각자 풀어온 문제들 중 가장 인상 깊었던 문제에 대해 공유합니다.

<br />

## Pull Request & Commit Rule

### PR Rule

- 이 Repository를 각자 Fork합니다.
- 각자의 닉네임으로 Fork한 Repository에서 branching합니다. (Ex. 'Jeckmu' 브랜치 생성)
- 푼 문제(+풀이과정, 설명)을 commit 후 PR 요청을 합니다.
- 각 팀의 미팅 시간에, 각 팀의 리더가 PR을 확인하고 Merge합니다.
- PR Message
  `[N주차] 닉네임` (Ex. `[1주차] Jeckmu`)

### Commit Rule

- 자신의 팀 폴더 - 주차 - (자신의 닉네임) 폴더에 알맞게 commit합니다.

  > 예시
  >
  > ```bash
  > Jeckmu
  > ├── [백준 - 1000] A+B
  > │   ├── [백준 - 1000] A+B.py
  > │   └── [백준 - 1000] 풀이.md
  > ```

- Commit Message
  1. 문제별로 하나씩 commit할 때는 `[N주차] [문제 사이트 - 문제 번호] 문제명`
     - Ex. `[1주차] [백준 - 1000] A+B`
  2. 주차별로 한번에 commit할 때는 `[N주차] 닉네임`
     - Ex. `[1주차] Jeckmu`

<br />

## File Structure (Example)

```bash
.
├── TEAM A
│   ├── Week 1
│   │   ├── Jeckmu
│   │   │   ├── [백준 - 1000] A+B
│   │   │   │   ├── [백준 - 1000] A+B.py
│   │   │   │   └── [백준 - 1000] 풀이.md
│   │   │   └── [백준 - 1005] ACM Craft
│   │   │       ├── [백준 - 1005] ACM Craft.py
│   │   │       └── [백준 - 1005] 풀이.md
│   │   ├── Ollie
│   │   │   ├── ...
│   │   │   └── ...
│   │   ├── ...
│   │   └── ...
│   ├── Week 2
│   │   ├── Jeckmu
│   │   └── ...
│   ├── ...
│   └── ...
├── TEAM B - Afternoon
│   ├── Week 1
│   │   ├── Swimmer
│   │   │   ├── ...
│   │   │   └── ...
│   │   ├── ...
│   │   └── ...
│   ├── ...
│   └── ...
└── TEAM B - Afternoon
    ├── Week 1
    │   ├── Shannon
    │   │   ├── ...
    │   │   └── ...
    │   ├── ...
    │   └── ...
    ├── ...
    └── ...
```

<br />

## History

### TEAM A

| 주차 | 테마                                                     | 문제 번호 및 이름                                            |
| :--- | :------------------------------------------------------- | :----------------------------------------------------------- |
| 1    | 백준 - 자유                                              | [백준] [1647. 도시 분할 계획 (Gold IV)](https://www.acmicpc.net/problem/1647)<br/>[백준] [1987. 알파벳 (Gold IV)](https://www.acmicpc.net/problem/1987) |
| 2    | 프로그래머스 - **2023 KAKAO BLIND RECRUITMENT** 기출문제 | [프로그래머스] [150369. 택배 배달과 수거하기 (Lv.2)](https://school.programmers.co.kr/learn/courses/30/lessons/150369)<br/>[프로그래머스] [150367. 표현 가능한 이진트리 (Lv.3)](https://school.programmers.co.kr/learn/courses/30/lessons/150367)<br/>[프로그래머스] [150365. 미로 탈출 명령어 (Lv.3)](https://school.programmers.co.kr/learn/courses/30/lessons/150365) |
| 3    | 프로그래머스 - **2023 KAKAO BLIND RECRUITMENT** 기출문제 | [프로그래머스] [150370. 개인정보 수집 유효기간 (Lv.1)](https://school.programmers.co.kr/learn/courses/30/lessons/150370)<br/>[프로그래머스] [150368. 이모티콘 할인행사 (Lv.2)](https://school.programmers.co.kr/learn/courses/30/lessons/150368)<br/>[프로그래머스] [150366. 표 병합 (Lv.3)](https://school.programmers.co.kr/learn/courses/30/lessons/150366)<br/>[프로그래머스] [150364. 1,2,3 떨어트리기 (Lv.4)](https://school.programmers.co.kr/learn/courses/30/lessons/150364) |

<br/>

### TEAM B - Morning, Afternoon

| 주차 | 테마          |
| ---- | ------------- |
| 1    | Stack / Queue |
| 2    | Brute-Force   |

