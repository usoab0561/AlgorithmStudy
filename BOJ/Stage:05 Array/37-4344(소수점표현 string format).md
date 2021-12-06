```swift
//
//  main.swift
//  Algorithm2
//
//  Created by hojang on 2021/12/06.
//

import Foundation

let C = Int(readLine()!)!

for _ in 1...C{
    let arr = readLine()!.split(separator: " ").map{ Double(String($0))! }
    var sum: Double = 0
    var ave: Double = 0 // 평균
    var ratio: Double = 0
    
    for i in 1 ... arr.count-1{
        sum = sum + arr[i]
    }
    
    sum = sum / Double(arr.count - 1) // 함수같은거 가져올때는 되게 strict해서 신경을 써줘야한다
    
    ave = sum * 1000 / 1000
    
    //dump(arr)
    //dump(ave)
    for i in 1 ... arr.count-1{
        if (arr[i] > ave){
            ratio += 1
        }
    }
    ratio = ratio / (Double(arr.count)-1) * 100
    
    print("\(String(format: "%.3f", ratio))%")
}
```
