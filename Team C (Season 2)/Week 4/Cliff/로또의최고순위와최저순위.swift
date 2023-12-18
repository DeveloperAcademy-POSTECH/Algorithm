func lottoWinningGrade(_ unpollutedLottos: [Int], _ win_nums: [Int]) -> Int {
    let wonCount = unpollutedLottos.compactMap { number in
        win_nums.contains(number) ? true : nil
    }.count
    
    return 7 - wonCount
}

func lottoMinMax(_ lottos: [Int], _ win_nums: [Int]) -> [Int] {
    // 예외 케이스 처리
    // 1. 전부 0인 경우 => [1, 6]
    // 2. 전부 꽉 찬 경우 => 숫자가 변할 수 없으므로 [등수, 등수]
    if lottos == [0, 0, 0, 0, 0, 0] {
        return [1, 6]
    } else if !lottos.contains(0) {
        let winCount = win_nums.compactMap { lottos.contains($0) ? true : nil }.count
        let grade = winCount > 0 ? 7 - winCount : 6
        return [grade, grade]
    }
    
    /*
     0이 1개인 경우
     당첨: 0 | ㅇ: 1 | oxxxxx [5(6), 5(7)] = 13
     당첨: 1 | ㅇ: 1 | *oxxxx [5, 5(6)] = 11
     당첨: 2 | ㅇ: 1 | **oxxx [4, 5] = 9
     당첨: 3 | ㅇ: 1 | ***oxx [3, 4] = 7
     당첨: 4 | ㅇ: 1 | ****ox [2, 3] = 5
     당첨: 5 | ㅇ: 1 | *****o [1, 2] = 3
     
     o = 1 일때 당첨 0이면 (합의) 최대값 13
     o = 2 일때 당첨 0이면 최대값 12
     o = 3 일때 당첨 0이면 최대값 11
     o = 4 일때 당첨 0이면 최대값 10
     o = 5 일때 당첨 0이면 최대값 9
     => 당첨 증가마다 합의 최대값으로부터 2 깎임
     
     최저값은 무조건 7(=>5로 대체)부터 시작, 당첨 증가시마다 1 감소
     */
    
    let zeroCount = lottos.filter { $0 == 0 }.count
    let winCount = win_nums.compactMap { lottos.contains($0) ? true : nil }.count
    print(lottos, win_nums, zeroCount, winCount)
    
    let sumOfMinMax = (14 - zeroCount) - (winCount * 2)
    let lowestGrade = 7 - winCount
    let highestGrade = sumOfMinMax - lowestGrade
    
    return [highestGrade, lowestGrade].map { $0 >= 6 ? 6 : $0 }
}

lottoMinMax([44, 1, 0, 0, 31, 25], [31, 10, 45, 1, 6, 19])
lottoMinMax([0, 0, 0, 0, 0, 0], [38, 19, 20, 40, 15, 25])
lottoMinMax([45, 4, 35, 20, 3, 9], [20, 9, 3, 45, 4, 35])

lottoMinMax([15, 27, 30, 0, 0, 0], [15, 27, 31, 12, 13, 14]) // [2, 5]
lottoMinMax([1, 2, 3, 4, 5, 6], [7, 8, 9, 10, 11, 12]) // [6, 6]
