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
        
myCar1= Car("빨강",30)
myCar2=Car("파랑",60)

mycar1=Car()

mycar1.color="파랑"
mycar1.speed=30

print(f"자동차1의 색상은 {mycar1.color}이고 속도는{mycar1.speed}이다.")

car2=Car("benz",30) #init value
namec1=car.getname()
