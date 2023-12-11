
#special method of class

class Line:
    length = 0
    
    
    def __init__(self,len=0): # Constructor duplication effect
        self.length=len
        print(self.length,'길이의 선이 생성되었습니다.')
        
    def __del__(self):# When calling the destructor
        print(self.length,'길이의 선이 삭제되었습니다.')
        
    def __repr__(self): #when calling the print func
        return "선의 길이: "+str(self.length)
    
    def __add__(self,other):# when calling operator '+' 
        return self.length+other.length
    
    def __lt__(self,other):# when calling compare operator
        return self.length <other.length
    
    def __eq__(self,other):
        return self.length == other.length
    
    
#메인코드부분
line1=Line(100) ##create obj -- allocate dinamic memory
line2=Line(200)## line1,2, is reference variable of pointer  indicating start address of obj
print(line1)
print("두 선의 길이 합:", line1.length+line2.length)

if line1.length< line2.length:
    print("선분 2가 더 기네요")
elif line1.length == line2.length:
    print("두 선분의 길이가 같네요")
    
else:
    print("모르겠네요")

del(line2) ## There is no separate dynamically allocated memory.
    
del(line1)
