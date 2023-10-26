import Foundation

// 기본 케이스는 맞는데 채점하면 실패
func delivery실패(_ cap: Int, _ n: Int, _ deliveries: [Int], _ pickups: [Int]) -> Int64 {
    var deliveries = deliveries
    var pickups = pickups
    var totalDistance = 0
    
    var remainCap = cap
    
    func moveToDeliveriesEnd() {
        // 오른쪽 끝으로 이동
        totalDistance += max(deliveries.count, pickups.count)
        while !deliveries.isEmpty {
            let lastDelv = deliveries.removeLast()
            print(#function, lastDelv)
            remainCap -= lastDelv
            print(#function, remainCap)
            if remainCap == 0 {
                remainCap = cap
                break
            } else if remainCap < 0 {
                deliveries.append(abs(remainCap))
                remainCap = cap
                break
            }
        }
    }
    
    func moveToPickupsEnd() {
        // 오른쪽 끝에서 왼쪽으로 이동
        totalDistance += pickups.count
        while !pickups.isEmpty {
            let lastPkup = pickups.removeLast()
            print(#function, lastPkup)
            remainCap -= lastPkup
            print(#function, remainCap)
            if remainCap == 0 {
                remainCap = cap
                break
            } else if remainCap < 0 {
                pickups.append(abs(remainCap))
                remainCap = cap
                break
            }
        }
    }
    
    while !deliveries.isEmpty && !pickups.isEmpty {
        // 왕복하면서, 배달 먼저, 수거 나중
        
        // 왕복 1회
        moveToDeliveriesEnd()
        moveToPickupsEnd()
    }
    
    return Int64(totalDistance)
}

func delivery(_ cap: Int, _ n: Int, _ deliveries: [Int], _ pickups: [Int]) -> Int64 {
    /*
     https://oh2279.tistory.com/147
     그리디 문제이다.

     예제 풀이를 따라 코드를 작성하면, 아마 시간초과가 발생할 것이다. n이 최대 100,000까지므로 n^2의 시간복잡도로는 문제를 풀 수 없다.

     우선, 한번에 최대한 멀리가서 멀리 있는 곳들의 작업을 먼저 끝내야지 이동횟수를 최소한으로 만들 수 있으므로 입력받은 배열들을 역순으로 뒤집어준다. 가장 먼 곳부터 탐색을 시작하는데, 배달해야 하거나 픽업해와야 할 것들이 하나라도 있으면 그곳으로 이동한다!

     어차피 한번 가면 다시 물류창고로 되돌아와야 하므로 정답에는 거리 x 2를 더해준다.

     이때 각 위치의 배달/픽업 값들에서 cap값을 빼준다. 이 연산의 결과들이 모두 음수라면 해당 위치의 배달/픽업 값이 한번에 실어 나를 수 있는 용량(=cap)보다 적은 것이므로, 오가는 길에 겸사겸사 추가적으로 배달/픽업이 가능하다는 의미이다!
     예) 수거해야할 택배상자가 2인데 cap이 4면 -2가 되고 이 2만큼 추가 적재가 가능하다

     때문에 have_to_deli, have_to_pick 값이 양수가 되기 전까진 이동이 필요 없고, 이 두 값 중 하나라도 양수가 될 때만 해당 위치로 이동해주면 된다.
     */
    
    var totalDistance = 0
   
    var reversedDelvs = Array(deliveries.reversed())
    var reversedPkups = Array(pickups.reversed())
    
    var haveToDelivery = 0
    var haveToPickup = 0
    
    for i in 0..<n {
        haveToDelivery += reversedDelvs[i]
        haveToPickup += reversedPkups[i]
        print("before:", i, haveToDelivery, haveToPickup)
        while haveToDelivery > 0 || haveToPickup > 0 {
            haveToDelivery -= cap
            haveToPickup -= cap
            totalDistance += (n - i) * 2
            print("while:", i, haveToDelivery, haveToPickup, totalDistance)
        }
    }
    
    return Int64(totalDistance)
}

delivery(4, 5, [1, 0, 3, 1, 2], [0, 3, 0, 4, 0]) // 16
// delivery(2, 7, [1, 0, 2, 0, 1, 0, 2], [0, 2, 0, 1, 0, 2, 0]) // 30
//
// delivery(2, 2, [0, 6], [0, 0]) // 12

