import Foundation

// 소수: 1과 자기 자신 만을 약수로 가지는 수들을 소수, 0과 1은 소수가 아님
func findPrime(_ numbers: String) -> Int {
    let oneDigitPrime = [2, 3, 5, 7].map(String.init)
    if numbers.count == 1 {
        if oneDigitPrime.contains(numbers) {
            return 1
        } else {
            return 0
        }
    }
    
    // 최대 자릿수 구하기
    let digit = numbers.count
    
    // 가능한 소수 모두 구하기
    // (소수 구할때 제곱근 이상이면 소수, 서로소가 아니라고 증명되었다.)
    let maxNumber = NSDecimalNumber(decimal: pow(10, digit)).intValue - 1
    let possibleAllPrimes = oneDigitPrime + (11...maxNumber).filter { number in
        var divided: [Int] = []
        for i in 1...maxNumber {
            if number % i == 0 {
                divided.append(number)
            }
        }
        
        return divided.count == 2
    }.map(String.init)
    
    let numberFilteredPrimes = possibleAllPrimes.filter { primeString in
        return primeString.map { primeChar in
            numbers.contains(primeChar)
        }.allSatisfy { $0 }
    }
    
    
    
    let d = numberFilteredPrimes.filter { f in
        print(f, possibleAllPrimes.contains(f))
        return possibleAllPrimes.contains(f)
    }
    
    
    return 0
}

findPrime("17")
// findPrime("011")
