#튜플은 리스트와 비슷하게 사용되는 파이썬의 대표적인 자료형.
#튜플은 한번 설정된 값을 변경할 수 없다.

tuple = (1,2,3)
print(tuple)

list1 = [1,2,3]
list2 = [4,5,6]

tuple = (list1,list2)
print(tuple)

#tuple ohject does not support Item assignment
# tuple[0] = 1

#튜플은 인덱싱과 슬라이싱이 가능함.
a = (0,1,2,3,4,5,6,7,8,9)
print (a[1])
print (a[0:5])

#튜플에 대한 연산도 가능함 -> 곱한 횟수만큼 출력함
print (a[0:5] * 3) 
