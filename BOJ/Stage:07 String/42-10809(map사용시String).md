```swift
//
//  main.swift
//  Algorithm2
//
//  Created by hojang on 2021/12/13.
//

import Foundation

let S = readLine()!.map{ String($0) }

var arr = Array(repeating: -1, count: 26)
// print(Character(S[0]).asciiValue! - 97)

for i in 0...S.count-1{
    let index = Int(Character(S[i]).asciiValue! - 97)
    if (arr[index] == -1){
        arr[index] = i
    }
}

arr.forEach{
    print($0, terminator: " ")
}

```
