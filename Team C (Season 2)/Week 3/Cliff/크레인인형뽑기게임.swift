func craneGame(_ board: [[Int]], _ moves: [Int]) -> Int {
    var board = board
    var basket: [Int] = []
    // 터진 횟수가 아니고 없어진 인형 총 개수임
    var removedDollCount = 0
    
    for indexOneBased in moves {
        let indexZeroBased = indexOneBased - 1
        
        for j in 0..<board.count {
            if board[j][indexZeroBased] == 0 {
                continue
            }
            
            basket.append(board[j][indexZeroBased])
            board[j][indexZeroBased] = 0
            break
        }
        
        // print("basket before:", basket)
        // 바스켓 업데이트
        if basket.count >= 2 && basket[basket.count - 1] == basket[basket.count - 2] {
            basket.removeLast()
            basket.removeLast()
            removedDollCount += 2
        }
        // print("basket after:", basket)
    }
    
    return removedDollCount
}

craneGame([
    [0,0,0,0,0],
    [0,0,1,0,3],
    [0,2,5,0,1],
    [4,2,4,4,2],
    [3,5,1,3,1]
],
          [1,5,3,5,1,2,1,4])