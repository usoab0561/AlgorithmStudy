```swift
//
//  main.swift
//  Algorithm2
//
//  Created by hojang on 2021/12/13.
//
// https://www.acmicpc.net/source/34668627
// dict로 수정해보자

import Foundation
// 65~90 : A~Z
// 97~.. : a~z

var arr = readLine()!
var arrCharacter: [Character] = []

var countArr = Array(repeating: 0, count: 26)

for char in arr{
    arrCharacter.append(char)
}

arrCharacter.forEach{
    var temp = -1
    if ($0.asciiValue! >= 65 && $0.asciiValue! <= 90){
        temp = Int($0.asciiValue! - 65)
    }else if ($0.asciiValue! >= 97 && $0.asciiValue! <= 97+25){
        temp = Int($0.asciiValue! - 97)
    }
    
    if (temp != -1){
        countArr[temp] += 1
    }
}
//print(countArr)
//print(countArr.firstIndex(of: countArr.max()!)!)
//print(countArr.lastIndex(of: countArr.max()!)!)

if (countArr.firstIndex(of: countArr.max()!)! !=
    countArr.lastIndex(of: countArr.max()!)! ){
    print("?")
}else{
    let c = Character(UnicodeScalar(countArr.firstIndex(of: countArr.max()!)! + 65)!)

    print(c)
}
```
