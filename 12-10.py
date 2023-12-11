class SuperClass:
    def method(self): #void mathod
        pass
class SubClass1(SuperClass):
    def method(self): ##redefine method
        print("subclass에서 method를 overriding ")
        
class SubClass2(SuperClass):
    def method(self):
        pass  ##  because childclassof abstract class , must doing method overriding

sub1=SubClass1()
sub2=SubClass2()

sub1.method()
sub2.method() ##No output because there is no method overriding.

#####
