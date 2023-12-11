from multiprocessing import Process, freeze_support
#way to declare it as a class
class HelloProcess(Process):
    def __init__(self):
        super(Process,self).__init__() # call Constructor of superclass
    
    def run(self): ## method run() : autorun
        print("Hello process2")
        
##maincode part
if __name__ == '__main__':
    freeze_support()
    p1=HelloProcess(1,arg2='Hello')
    p1.start()
    p1.join()
    p1.terminate()