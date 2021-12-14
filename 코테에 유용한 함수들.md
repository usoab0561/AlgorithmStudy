
# 배열

## element중 첫번째 index 찾기
```swift
arr.firstIndex(of: something + 1)! // it returns as optional Int
```

## foreach 로 컨테이너 돌기 
```swift
arr.forEach{
  print($0)
}
```

## 중복피하기 set
```swift
var setProperty = Set(arr)
print(set.count) // 중복없는 array 개수 보여준다
```

## string을 배열로 각각 넣어주기
```swift
var arr = readLine()!.map{String($0)} // 입력 바로 받을때
var arr = readLine()!.map(String.init) // 입력 바로 받을때

var strings: String = "abcdefg"
var arr3: [String] = strings.map{String($0)} 

```

## 소수점표현 string format
```swift
String(format: "%.3f", wantToShow)
```

# 문자열

## asciicode로 변환
```swift
print(Character(readLine()!).asciiValue!)
```

## 뒤집기
```swift
let num = readLine()!.split(separator: " ")
let a = Int(String(num[0].reversed()))! // 123 456 -> 321
```

# readLine시 한번에 형변환 하기

```swift
let a = readLine()!.split(separator: " ").map(Int(String($0))!)
```

