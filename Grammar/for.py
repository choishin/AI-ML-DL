#파이썬에서 반복문은 range(시작,끝)으로 표현됨
for i in range(1,10):
    print(i)

#몇개 포함되어있나 세기
count=0;
for i in "Hello World":
    if i == 'o':
        count = count+1
print("o의 개수는 ",count,"개 입니다.")

#전체 합 구하기 (※i가 인덱스가 아님)
sum = 0;
list = [0,1,2,3,4,5]
for i in list :
    sum = sum + i
print(sum)

#continue, break 사용하기
sum = 0
list = [1,2,3,4,5]
for i in list:
    sum = sum+i
    if sum >= 5:
        break;
print(sum)