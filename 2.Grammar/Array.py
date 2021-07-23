#list(리스트) -> 리스트 형식을 반환
a = [10,20,30,40,50]
print(list(a))

#count(찾는원소) -> 원소의 갯수를 반환합니다
print(a.count(10))

#index(찾는원소) -> 원소의 위치를 반환합니다
print(a.index(50))

#append(추가할원소) -> 배열에 추가
a.append(60)
print(list(a))

#sort(키,역순여부) -> 원소를 정렬
a = [9,5,3,2,6,7,1,8,4,6]
a.sort()
print(list(a))

#extend(리스트) -> 다른 리스트와 합치기
a = [0,1,2,3,4]
b = [5,6,7,8,9]
a.extend(b)
print(list(a))

#insert(위치,원소) -> 특정 위치에 원소를 넣기
a = [0,1,2,3,4]
a.insert(3,5)
print(list(a))

#remove(원소) -> 원소를 삭제
a.remove(5)
print(list(a))

#pop(위치) -> 특정위치의 원소를 꺼내기
a = [8,7,4,3,2]
a.pop(2)
print(list(a))

#reverst() -> 리스트를 뒤집기
a = [8,7,4,3,2]
a.reverse()
print(list(a))