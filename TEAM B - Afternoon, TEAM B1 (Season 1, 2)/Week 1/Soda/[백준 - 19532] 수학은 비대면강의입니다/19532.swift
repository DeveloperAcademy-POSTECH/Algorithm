//
//  19532.swift
//  Algorithm
//
//  Created by 김민 on 2023/04/30.
//
// 브루트 포스 - 19532 수학은 비대면 강의입니다 ~!

// 1. 브루트포스로 일단 풀어볼게여

//let nums: [Int] = readLine()!.split(separator: " ").map { Int($0)! }
//
//for x in -999...999 {
//    for y in -999...999 {
//        if (nums[0] * x + nums[1] * y == nums[2]) && (nums[3] * x + nums[4] * y == nums[5]) {
//            print(x, y)
//            break
//        }
//    }
//}

// 2. 연립방정식은 가감법...으로 많이 푼대여

let nums: [Int] = readLine()!.split(separator: " ").map { Int($0)! }
let (a, b, c, d, e, f) = (nums[0], nums[1], nums[2], nums[3], nums[4], nums[5])
let x = (c * e - b * f) / (a * e - b * d)
let y = (c * d - a * f) / (b * d - a * e)
print(x, y)
