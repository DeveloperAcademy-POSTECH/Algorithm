import Foundation

func truckPassingTheBridge(_ bridge_length: Int, _ weight: Int, _ truck_weights: [Int]) -> Int {
    if truck_weights.count == 1 {
        return bridge_length + 1
    }
    
    var seconds = 0
    var sumOfBridge = 0 // 시간초과 방지용
    var truckWeightsQueue = truck_weights
    var bridge = [Int](repeating: 0, count: bridge_length)
    
    while !bridge.isEmpty {
        seconds += 1
        sumOfBridge -= bridge.removeFirst()
        
        if !truckWeightsQueue.isEmpty {
            if sumOfBridge + truckWeightsQueue[0] <= weight {
                let firstTruck = truckWeightsQueue.removeFirst()
                bridge.append(firstTruck)
                sumOfBridge += firstTruck
            } else {
                bridge.append(0)
            }
        }
    }
    
    return seconds
}

truckPassingTheBridge(2, 10, [7, 4, 5, 6])
truckPassingTheBridge(100, 100, [10])
truckPassingTheBridge(100, 100, [10, 10, 10, 10, 10, 10, 10, 10, 10, 10])
