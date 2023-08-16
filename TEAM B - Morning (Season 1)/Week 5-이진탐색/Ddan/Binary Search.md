# Binary Search
Binary Search란 탐색할 자료를 둘로 나누어, 해당 데이터가 있을 곳을 탐색하는 것이다.

중요한 것은 탐색할 자료가 이미 정렬되어 있을 때만 사용 가능하다.

완전 탐색 알고리즘은 최악의 경우 모든 배열을 탐색하기 때문에, 시간 복잡도가 O(n)으로 성능이 좋진 않다. 반면 이진탐색(Binary Search)은 완전 탐색보다 좋은 성능을 갖고 있다. -> O(logN)

## 이해 돕기
이해를 돕기 위해 오름 차순으로 정렬된 배열에서 '35'를 이진탐색을 통해 찾아보자.

<img width="518" alt="image" src="https://github.com/eemdeeks/eemdeeks/assets/87136217/6d2d50c4-71fb-4e54-ae1d-92053a5a5ada">

가장 먼저 mid를 기준으로 반으로 나눈다.

<img width="518" alt="image" src="https://github.com/eemdeeks/eemdeeks/assets/87136217/309d70aa-6d7a-452a-9ad9-13de67ad122f">

여기서 mid의 index는 배열크기/2로 계산한다.

mid를 기준으로 반으로 나눴으면 mid와 찾는 값을 비교한다. 위의 예시에서는 35를 찾는 것이므로 mid인 20과 35를 비교하면 mid보다 35가 크므로 나눠진 배열에서 오른쪽 배열을 위와 같은 작업을 반복한다. (정렬이 되어 있으므로 20보다 작은 왼쪽에는 원하는 데이터가 없다는 것을 알기 때문에.)

이와 같은 행동을 반복하다 mid가 35인 경우에 true를 반환하는 것이다.

근데, 이 행위를 반복하다 데이터가 1개만 남았을 경우에는, 데이터를 비교 후 같지 않다면 false를 반환하는 것이다.

## 코드로 구현해보기
위 예시를 보면 재귀함수나 반복문으로 구현하면 편할 것 같다는 생각이 들것이다.

반복문이나 재귀함수로 지속해서 반으로 나누고 비교하고를 반복하다가, 결국 데이터가 하나 남았을 때 종료시키면 될 것 같다.

바로 구현해보자.

### ex) 재귀함수
```swift
func binarySearchRecursive(_ array: [Int], num: Int) -> Bool {
    guard array.count != 1 else {
        return array[0] == num ? true : false
    }
    let mid = array.count / 2
    guard array.count != 2 || array[1] > num else {
        return false
    }
    if array[mid] == num { return true }
    let range = array[mid] > num ? (0..<mid) : ((mid+1)..<array.count)
    return binarySearchRecursive(Array(array[range]), num: num)
}
```

### ex) 반복문
```swift
func binarySearchIteration(_ array: [Int], num: Int) -> Bool {
    var start = 0
    var end = (array.count - 1)
    
    while start <= end {
        let mid = (start + end) / 2
        
        if array[mid] == num { return true }
        if array[mid] > num {
            end = mid - 1
        } else {
            start = mid + 1
        }
    }
    return false
}
```
