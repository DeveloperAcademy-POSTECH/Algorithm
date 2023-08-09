import Foundation


func solution(_ array:[Int], _ commands:[[Int]]) -> [Int] {
    var returnArray: [Int] = []
    var temp = 0
    for command in commands {
        // slice 대신 append 하기
        var slicedArray: [Int] = []
        for i in command[0]-1 ..< command[1]{
            slicedArray.append(array[i])
        }
//        slicedArray.sort()
        // 연습을 위해 직접 정렬 구현
        // slicedArraydml sort 구현 - bubbleSort
        for i in 0..<slicedArray.count {
            for j in 0..<(slicedArray.count-1-i){
                if slicedArray[j] > slicedArray[j+1]{
                    slicedArray.swapAt(j, j+1)
                }
            }
        }
        returnArray.append(slicedArray[command[2]-1])
        
    }
    return returnArray
}



/*
  실수했던 코드 - append 대신 slicing 이용했을때
  commands[1] 의 테스트 케이스와 같은 조건을 만족하지 못함.
*/

//func solution(_ array:[Int], _ commands:[[Int]]) -> [Int] {
//    var returnArray : [Int]  = []
//    for command in commands {
//        // slice
//        var slicedArray = array[command[0] - 1 ..< command[1]]
//        // sort
//        slicedArray.sort()
//        // k 번째 요소 apped
//        returnArray.append(slicedArray[command[2] - 1])
//    }
//    return returnArray
//}
//
