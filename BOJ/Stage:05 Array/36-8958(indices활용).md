```swift
//
//  main.swift
//  Algorithm2
//
//  Created by hojang on 2021/12/05.
//

import Foundation

let N = Int(readLine()!)!

for _ in 1...N{
    let arr = readLine()! // return value is optional String
    var count = 0
    var sum = 0
    
    for i in arr.indices{ // OXOOXOOXO -> [ O, X, O, O, ... ] 
        if("O" == arr[i]){
            count += 1
            sum += count
        }else{
            count = 0
        }
    }
    print(sum)
}
```
