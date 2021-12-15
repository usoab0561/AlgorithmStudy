```swift
//
//  main.swift
//  Algorithm2
//
//  Created by hojang on 2021/12/15.
//

func convertNumber (a: Character) -> Int{
    
    switch(a){
    case "A"..."C":
        return 3
    case "D"..."F":
        return 4
    case "G"..."I":
        return 5
    case "J"..."L":
        return 6
    case "M"..."O":
        return 7
    case "P"..."S":
        return 8
    case "T"..."V":
        return 9
    case "W"..."Z":
        return 10
    default:
        return 0
    }
}

let inputs = readLine()!
var sum = 0

inputs.forEach{
    sum += convertNumber(a: $0)
}

print(sum)
```
