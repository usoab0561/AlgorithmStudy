```swift
//
//  main.swift
//  Algorithm2
//
//  Created by hojang on 2021/11/25.
//

import Foundation
//프로그램의 종료 지점을 명시하지 않은 문제
// https://itllbegone.tistory.com/9
while let input = readLine(){
    let inputArr = input.split(separator: " ")
    let A = Int(inputArr[0])!
    let B = Int(inputArr[1])!
    
    print(A+B)
}

```
