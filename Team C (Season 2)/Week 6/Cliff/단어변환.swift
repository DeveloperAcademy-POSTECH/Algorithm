/*
 https://school.programmers.co.kr/learn/courses/30/lessons/43163
 
 문제 설명
 두 개의 단어 begin, target과 단어의 집합 words가 있습니다. 아래와 같은 규칙을 이용하여 begin에서 target으로 변환하는 가장 짧은 변환 과정을 찾으려고 합니다.

 1. 한 번에 한 개의 알파벳만 바꿀 수 있습니다.
 2. words에 있는 단어로만 변환할 수 있습니다.
 예를 들어 begin이 "hit", target가 "cog", words가 ["hot","dot","dog","lot","log","cog"]라면 "hit" -> "hot" -> "dot" -> "dog" -> "cog"와 같이 4단계를 거쳐 변환할 수 있습니다.

 두 개의 단어 begin, target과 단어의 집합 words가 매개변수로 주어질 때, 최소 몇 단계의 과정을 거쳐 begin을 target으로 변환할 수 있는지 return 하도록 solution 함수를 작성해주세요.

 제한사항
 각 단어는 알파벳 소문자로만 이루어져 있습니다.
 각 단어의 길이는 3 이상 10 이하이며 모든 단어의 길이는 같습니다.
 words에는 3개 이상 50개 이하의 단어가 있으며 중복되는 단어는 없습니다.
 begin과 target은 같지 않습니다.
 변환할 수 없는 경우에는 0를 return 합니다.
 입출력 예
 begin    target    words    return
 "hit"    "cog"    ["hot", "dot", "dog", "lot", "log", "cog"]    4
 "hit"    "cog"    ["hot", "dot", "dog", "lot", "log"]    0
 
 https://velog.io/@euneun/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EB%8B%A8%EC%96%B4-%EB%B3%80%ED%99%98BFSDFS-C-v5lnyekn
 
 이렇게 예제 1번의 풀이과정을 가시화시켜보면 하나의 줄기를 탐색해나가며 변환단계의 최소값을 구하면 된다는 것을 알 수 있다.

 하나의 줄기씩 한 방향으로 갈 수 있을때까지 탐색해나가므로 dfs 풀이법을 떠올릴 수 있다.
 변환 단계의 최소값이므로 한번 사용한 단어는 재사용하지 않는것이 암묵적인 규칙임을 알 수 있다. (단어를 재사용하면 변환단계가 더 길어지므로 최소값이 될 수 없으므로 해가 될 수 없다.)
 -> 따라서 단어별로 방문여부를 체크할 배열이 필요하다.
 탐색함수를 재귀적으로 호출해나가면서 target단어와 같아졌을때는 함수호출을 종료하는 종료조건을 염두해둔다.
 문제에서 한 번에 한 개의 알파벳만 바꿀 수 있다고 하였다. 따라서 하나의 줄기씩 탐색을 해나갈때 words 벡터에서 현재의 단어와 한글자만 다른 단어만이 탐색 후보가 될 수 있으므로 다른 문자가 한개인지 판별하는 함수도 작성해야한다.
 
 문제 풀이 방법
 1. 가장 간단해 보이는 다른문자가 한개인지 판별하는 함수부터 작성해보자.
 2. 재귀함수를 작성해보자.
  - 해당 탐색과정에서 다시 가장 가까운 갈림길로 돌아와서 (back-tracking) 이곳부터 다른 방향으로 다시 탐색을 진행해야한다
 
 [리뷰]
 1. 자력으로 못품 - 블로그보고 베낌 (설명 위주로 보고)
 2. 외부 반례는 찾지 않고 80% 정답률일때 스스로 나머지 20% 해결
 */

extension String {
    subscript(_ index: Int) -> Character? {
        guard index >= 0, index < self.count else {
            return nil
        }

        return self[self.index(self.startIndex, offsetBy: index)]
    }
}

func onlyOneDifferent(_ lhs: String, _ rhs: String) -> Bool {
    guard lhs.count == rhs.count else {
        return false
    }
    
    var result = 0
    for i in 0..<lhs.count {
        if lhs[i] == rhs[i] {
            result += 1
        }
        
        // 주의: 단어 수는 3~10자
        if result == lhs.count - 1 {
            return true
        }
    }
    
    return false
}

func convertWord(_ begin: String, _ target: String, _ words: [String]) -> Int {
    guard words.contains(target) else {
        return 0
    }
    
    var visited: Set<String> = []
    var result = Int.max // words.count의 최대값
    
    func dfs(_ begin: String, _ target: String, _ step: Int) {
        if begin == target {
            result = min(step, result)
            return
        }
        
        if step > result {
            return
        }
        
        for word in words {
            if onlyOneDifferent(begin, word) && !visited.contains(word) {
                // 백트래킹: 밑으로 갈 때는 방문 표시했다가, 다시 위로 역류하는 경우 방문 표시 해제
                visited.insert(word)
                dfs(word, target, step + 1)
                visited.remove(word)
            }
        }
    }
    
    dfs(begin, target, 0)
    
    return result != Int.max ? result : 0
}


convertWord("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]) // 4
convertWord("hit", "cog", ["hot", "dot", "dog", "lot", "log"]) // 0

convertWord("hit", "hit", ["hot", "dog"]) // 0
convertWord("hit", "cog", ["hot", "cog"]) // 0
convertWord("hit", "lot", ["hot", "lot"]) // 2
convertWord("willow", "solloy", ["wollow", "solloy", "wolloy", "willew"]) // 3
