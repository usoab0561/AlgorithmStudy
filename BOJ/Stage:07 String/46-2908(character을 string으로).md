```swift
import Foundation

let inputs = readLine()!.split(separator: " ")
var firstInput: [Character] = []
var secondInput: [Character] = []
var temp: Character

for char in inputs[0]{
    firstInput.append(char)
}

for char in inputs[1]{
    secondInput.append(char)
}

temp = firstInput[0]
firstInput[0] = firstInput[2]
firstInput[2] = temp


temp = secondInput[0]
secondInput[0] = secondInput[2]
secondInput[2] = temp

var firstInputString = String(firstInput)
var secondInputString = String(secondInput)

if (Int(firstInputString)! > Int(secondInputString)!){
    print(firstInputString)
}else{
    print(secondInputString)
}
```
  
reversed를 사용해서 간편하게 풀 수 있다.  

```swift
let num = readLine()!.split(separator: " ")
let a = Int(String(num[0].reversed()))!
let b = Int(String(num[1].reversed()))!

if a > b {
    print(a)
} else {
    print(b)
}
```
