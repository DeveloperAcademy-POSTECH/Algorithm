- [level 2] Title: H-Index
- [문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/42747)
```py
def solution(citations):
    arr = sorted(citations)
    for idx, h in enumerate(arr):
        if h >= len(arr) - idx:
            return len(arr) - idx

    return 0

#     첫 시도 멸망
#     answer = 0
#     arr = sorted(citations)
#     idxs = []

#     # print(arr)
#     for idx in range(0,len(arr)):
#         h = arr[idx]
#         if h <= len(arr[idx:]) and len(arr[:idx-1]) <= h:
#             # print(len(arr[idx:]), len(arr[:idx-1]), idx)
#             idxs.append(h)

#     # print(idxs)
#     return max(idxs)
```
---

- [level 1] Title: K번째수
- [문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/42748?language=python3)
```py
def solution(array, commands):
    answer = []
    for each in commands:
        answer.append(sorted(array[each[0]-1:each[1]])[each[2]-1])
    return answer
```

- 4673, 셀프 넘버
```py
arr = [i for i in range(0,10001)]
tmp = []

for i in arr:
    # 생성자 확인하기
    selfNum = i + sum(map(int, str(i)))
    # 생성자가 없으면 나중에 지우기
    if selfNum <= 10000:
        tmp.append(selfNum)

answer = set(arr) - set(tmp)
for num in sorted(list(answer)):
    print(num)
```

- [level 2] 조이스틱
- [문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/42860) 
```swift
import Foundation

func solution(_ name: String) -> Int {
    let alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    let alphabetReversed = Array(alphabet.reversed())
    var answer = 0

    // 위아래 움직임
    let _ = name.map {
        (min(alphabet.firstIndex(of: String($0))! - 1, alphabetReversed.firstIndex(of: String($0))!) + 1,
         String($0))
    }.forEach {
        answer += $0.0
    }

    // 좌우 움직임
    let nameArr = name.map { String($0) }
    var minimum = nameArr.count - 1

    for i in 0 ..< nameArr.count {
        var tmp = i + 1
        while tmp < nameArr.count, nameArr[tmp] == "A" {
            tmp += 1
        }

        let numberOfA = nameArr.count - tmp
        let goRight = i * 2 + numberOfA
        let goLeft = numberOfA * 2 + i

        minimum = min(minimum, goRight)
        minimum = min(minimum, goLeft)
    }
    return answer + minimum
}
```
