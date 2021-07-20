#파이썬은 객체지향을 기반으로한 인터프리터 언어이기 때문에, 객체지향의 기본단위인 class역시 있음.
#클래스를 인스턴스로 만들어서 사용
class Car1:
    def __init__(self, name, color):
        self.name = name
        self.color = color
    def show_info(self):
        print("이름:",self.name,"/색상 :",self.color)

car1 = Car1("소나타", "빨간색")
car1.show_info()

#getter/setter 설정
class Car2:
    def __init__(self, name, color):
        self.name = name
        self.color = color
    def show_info(self):
        print("이름:",self.name,"/색상 :",self.color)
    def get_name(self):
        return self.name
    def set_name(self, name):
        self.name = name

car2 = Car2("소나타", "빨간색")
print(car2.get_name())
car2.set_name("아반떼")
print(car2.get_name())

#Class의 소멸자
class Car3:
    def __init__(self, name, color):
        self.name = name
        self.color = color
    def get_name(self):
        return self.name
    def set_name(self, name):
        self.name = name
    def show_info(self):
        print("이름:",self.name,"/색상 :",self.color)
    def __del__(self):
        print("인스턴스를 소멸시킵니다")

car3 = Car3("소나타", "빨간색")
car3.show_info()
del car3

#Class의 상속
class Unit :
    def __init__(self,name,power):
        self.name = name
        self.power = power
    def attack(self) :
        print(self.name, "이(가) 공격을 수행합니다. [공격력:",self.power,"]")
#상속을 표현할때 class 이름(상속받을 부모)
class Monster(Unit):
    def __init__(self, name, power, type):
        self.name = name
        self.power = power
        self.type = type
    def show_info(self):
        print("몬스터 이름:",self.name,"/몬스터 종류 :",self.type)

monster = Monster("슬라임",10,"초급")
monster.show_info()
monster.attack()



