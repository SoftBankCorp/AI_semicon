class Car:
    color = ""
    speed =0
    value =0
    
    def upSpeed(self,value):
        self.speed+=value
    
    def downSpeed(self,value):
        self.speed -=value
        
mycar1=Car()

mycar1.color="파랑"
mycar1.speed=30

print(f"자동차1의 색상은 {mycar1.color}이고{mycar1.upSpeed(30)}속도는{mycar1.speed}이다.")