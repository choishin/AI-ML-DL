#print()
print("Hello python")
var = "Hello World"
print(var)

#백슬래쉬+" -> 따옴표 출력하기
print("\"안녕\" 파이썬!")

#String 연산
a = "안녕"
b = "파이썬"
print(a+b)

#String 곱하기도 가능 함...(대박)
a = "*"
print(a*10)

#인덱싱 (마이너스를 붙이면 뒤에서부터 센 결과를 보여줌)
a = "Hello World"
print(a[0]+a[1])
print(a[-1])

#슬라이싱 ([시작번호:마지막번호])
a = "Hello World"
print(a[2:9])
print(a[3:])
print(a[:-2])
print(a[0:7:2])

#replace()메소드
a = "Hello World"
b = a.replace("Hello","Hi")
print(b)

#count()메소드
s= "Hello"
print(s.count("l"))

#find()메소드 -> 찾는 문자열의 위치를 반환
fullStr = "Hello, Can you find me?"
findStr = "find"
index= fullStr.find(findStr)
print("Found : ",index)

#upper()
fullStr = "Hello, Can you find me?"
print(fullStr.upper())

#lower()
fullStr = "Hello, Can you find me?"
print(fullStr.lower())

#Strip() -> 부분 문자열을 지운 결과를 반환
fullStr = "Hello, Can you find me?"
print(fullStr.strip("Hello,"))

#Split()
fullStr = "Hello, Can you find me?"
s = fullStr.split(" ")
print(s)

#zfill()-> 자릿수만큼 나머지를 0으로 채움
result = "999"
print(result.zfill(10))

#int() -> 문자열로 표현된 숫자를 숫자형태로 바꿔줌
a = "789"
b = int(a)
print(b+1)

#파이썬에서 한글 표현이란...
a = "안녕하세여"
print(a)
