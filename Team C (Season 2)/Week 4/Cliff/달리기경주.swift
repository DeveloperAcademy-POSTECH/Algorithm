func runningRace(_ players: [String], _ callings: [String]) -> [String] {
    // 해설진이 부르면 추월 소환
    // 50000 * 1000000 = 500억으로 이중반복 불가능해 보임
    
    var players = players
    /// 플레이어 현재 인덱스 저장한 딕셔너리(해셔블)
    var playersCurrentIndexDict: [String: Int] = [:]
    
    for (index, player) in players.enumerated() {
        playersCurrentIndexDict[player] = index
    }
    playersCurrentIndexDict
    // 호명한 순서대로 추월 처리: O(1+x)
    for calling in callings {
        let overtakePlayerIndex = playersCurrentIndexDict[calling]!
        let beOvertakedPlayer = players[overtakePlayerIndex - 1]
        
        // swapAt: O(1)
        players.swapAt(overtakePlayerIndex, overtakePlayerIndex - 1)
        playersCurrentIndexDict[calling]! -= 1
        playersCurrentIndexDict[beOvertakedPlayer]! += 1
    }
    
    return players
}

runningRace(["mumu", "soe", "poe", "kai", "mine"], ["kai", "kai", "mine", "mine"])
