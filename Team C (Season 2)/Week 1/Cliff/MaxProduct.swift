import UIKit

let i1 = [[60, 50], [30, 70], [60, 30], [80, 40]]
let i2 = [[10, 7], [12, 3], [8, 15], [14, 7], [5, 15]]
let i3 = [[14, 4], [19, 6], [6, 16], [18, 7], [7, 11]]

func solution(_ sizes:[[Int]]) -> Int {
    /*
     10 7
     12 3
     8 15
     14 7
     5 15
     =>
     7 10
     3 12
     8 15
     7 14
     5 15
     =====
     14 4
     19 6
     6 16
     18 7
     7 11
     =>
     4 14
     6 19
     6 16
     7 18
     7 11

     오름차순으로 정렬 후 각 라인에서 가장 큰 값들을 곱함
     */
    var maxInSmalls: Int = 0
    var maxInLarges: Int = 0
    
    for size in sizes {
        let small = min(size[0], size[1])
        let large = max(size[0], size[1])
        
        maxInSmalls = max(small, maxInSmalls)
        maxInLarges = max(large, maxInLarges)
    }
    
    return maxInSmalls * maxInLarges
}
solution(i1)
solution(i2)
solution(i3)