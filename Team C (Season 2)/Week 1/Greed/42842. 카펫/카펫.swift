import Foundation

func solution(_ brown:Int, _ yellow:Int) -> [Int] {
    var t : Int = (brown - 4)/2
    var answer : [Int] = []
    
    for i in 1...t {
        var width : Int = t - i
        var height : Int = i
        if width * height == yellow && width >= height {
            answer = [width + 2, height + 2]
        }
    }
    
    
    return answer
}