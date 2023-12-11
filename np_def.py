#define multiprocess as funtion

from multiprocessing import Process,freeze_support

def Hello():
    print("hello process")
    
    
if __name__=='__main__':
        freeze_support() ## call function that need to mutiprocessing at windows OS
        
        p1=Process(target=Hello)
        p1.start() #start process
        p1.join() # pause until process finished
        p1.terminate() ## process termination