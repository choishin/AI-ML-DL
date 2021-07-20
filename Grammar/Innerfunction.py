#input() -> 자바의 Scanner
user_input = input('정수를 입력하세요 : ')
print("제곱:", int(user_input)**2)

#int() -> 문자열, 실수 등 자료형을 정수형으로 바꿔줌
a = "12345"
print(int(a)+1)

#float() -> 문자열,정수 등 자료형을 실수형으로 바꿔줌
a="123.45"
print(float(a)+0.5)

#max()/min()
list=[5,6,3,2,9,8,4,1,7]
print(max(list))
print(min(list))
print("\n")

#bin() -> 10진수를 2진수로 변환할 때 / hex()->10진수를 16진수로 변환할 때 (반환값은 문자열임)
print(bin(128))
print(hex(230))
print(int('0xe6',16))

#round() -> 반올림 함수
print(round(123.789))

#type() -> 자료형이 무엇인지 알려주는 역할
int = 1
str = "문자열"
list = [1,2,3]
dict = {'apple': '사과','banana': '바나나'}
print(type(int))
print(type(str))
print(type(list))
print(type(dict))
