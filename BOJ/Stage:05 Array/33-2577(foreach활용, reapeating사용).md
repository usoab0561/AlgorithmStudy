```swift
//
//  main.swift
//  Algorithm2
//
//  Created by hojang on 2021/11/26.
//

import Foundation

let inputA = Int(readLine()!)!
let inputB = Int(readLine()!)!
let inputC = Int(readLine()!)!
var sum = inputA * inputB * inputC
var arr: [Int] = [Int](repeating: 0, count: 10)

while sum > 0{  // sum을 modulation한뒤 그것을 index로 사용한다.
    let i = sum % 10
    arr[i] += 1
    sum /= 10
}

/*
for i in 0...arr.count-1{ // foreach로 바꿔보자.
    print(arr[i])
}
*/

arr.forEach{
    print($0) // 이게 인덱스 돌면서 클로저를 파라미터로 넘겨줌. 함수임.
             // for in이랑 다름.
            // https://babbab2.tistory.com/95
}

```
