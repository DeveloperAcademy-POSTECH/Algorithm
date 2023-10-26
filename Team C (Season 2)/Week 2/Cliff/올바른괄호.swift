import Foundation

func correctBracket실패(_ s:String) -> Bool {
    var sArr = s.map(String.init)
    
    if sArr.count == 0 || sArr.count % 2 == 1
        || sArr[0] == ")" || (sArr[sArr.count - 1] == "(") {
        return false
    }
    
    var leftStack: [String] = Array(sArr.reversed())
    var rightStack: [String] = []
    
    while leftStack.count > 0 {
        guard let popped = leftStack.popLast() else {
            return false
        }
        
        if rightStack.count >= 1 && popped == ")" {
            if let rightLast = rightStack.last {
                
                if !leftStack.isEmpty {
                    if let rightPopped = rightStack.popLast(), rightPopped == "(" {
                        continue
                    } else {
                        return false
                    }
                }
            }
        }
        
        rightStack.append(popped)
    }

    return sArr.filter({ $0 == "(" }).count == sArr.count / 2
}

func correctBracket(_ s: String) -> Bool {
    var stack: [String] = []
    var sArr = s.map(String.init)
    
    for i in 0..<s.count {
        if sArr[i] == "(" {
            stack.append("(")
        } else {
            if stack.isEmpty {
                return false
            }
            
            stack.popLast()
        }
    }
    
    return stack.isEmpty
}

correctBracket("()()")
correctBracket("(())()")
correctBracket(")()(")
correctBracket("(()(")

correctBracket("(()))")
correctBracket("(((((((")
correctBracket(")))))))))")
correctBracket("()")
correctBracket("(())")
correctBracket("(")
correctBracket(")")
correctBracket(")(")
correctBracket("((())())")

// 5, 11 ())(()
correctBracket("())(()")
/*
 
 */
correctBracket("()()()()")
