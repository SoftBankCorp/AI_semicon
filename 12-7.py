#class inheritance
#매개변수가 있는 생성자
#constructor with parameter

class Car:
    color = ""
    speed=0
    name=""
    
    def __init__(self,value1,value2):
        self.color=value1
        self.speed=value2
    
    def getName(self):
        return self.name
    
    def getSpeed(self):
        return self.speed
    
    def upspeed(self,value):
        self.speed+=value
        print(f"현재 속도(슈퍼클래스)는 {self.speed}km 입니다.")

class Sedan(Car) : #car 클래스 상속받음 . 자식클래스
    def upspeed(self, value):
        self.speed+=value
        
        if self.speed>=150:
            self.speed=150
            
        print(f"현재속도(자식클래스)는 {self.speed}")

class Truck(Car):
    pass  #not data in Truck class . because use to block error
#mean that inherit just superclass

sedan1,truck1=None,None
sedan1= Sedan()
truck1=Truck()

truck1.upSpeed(200)#슈퍼 클래스 출력
    
        
#myCar1= Car("빨강",30)
#myCar2=Car("파랑",60)

#mycar1=Car()

#mycar1.color="파랑"
#mycar1.speed=30

#print(f"자동차1의 색상은 {mycar1.color}이고 속도는{mycar1.speed}이다.")


