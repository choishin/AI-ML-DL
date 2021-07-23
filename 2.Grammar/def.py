#파이썬에서는 function도 method도 아니고, def로 함수를 선언함.
#리턴이 있는 경우
def add (a,b) :
    return a+b

print(add(1,3))

#리턴이 없는 경우(void)
def add_print(a,b):
    print(a+b)

add_print(1,4)

#전역변수 global 키워드를 써주면 됨.
def add():
    global a
    a = a +5
a = 2
add()
print(a)

#가변인자가 함수의 파라미터로 들어오는 경우 *를 붙여준다.
#무슨소리인지 정확히 모르겠음. 하다보면 알겠지...?
def function(*data):
    print(data)

function(1,2,3)

#파이썬의 함수는 반환값이 여러개 일 수 있는 특징이 있는데, 반환값이 여러개인 경우, 튜플 형태로 반환됨.
def function():
    a = 5
    b = [1,2,3]
    return a,b
a,b = function()
print(a)
print(b)
#튜플 아닌데? 이것도 차차 이해하기로 함.
b[0] = 0
print(b)