import multiprocessing as mp
import time

 ###funtion wating condition
 ### A program that makes three processes wait and wakes them up using the same condition object.
 
 ## p1,p2,p3 프로세스를 만들고 p3가 p1,p2를 깨우는 역할 담당.
 #method: acquire(), wait(), notifiy_all(),release(),notify() 
 #notify() : 둘중에 걸리는 거 아무나 실행하는 거
 
def pro1(c,pn):
    c.acquire() ##acqiure codition obj
    c.wait()  ##wait until specific codition is 
    print (f"{pn} 프로세스의 기다림이 끝났습니다. pro1동작 중...")
    c.release() ## release codition obj
    pass
 
def pro2(c,pn):
    c.acquire() ##acquire condition obj
    #c.notify_all() ## role that awake all processes (p1,p2)
    c.notify() ## role that awake random one of  processes (p1,p2)
    
    c.release()
    pass



if __name__ =='__main__':    
    cond = mp.Condition()
    p1 = mp.Process(target=pro1, args=(cond, 'p1'))
    p2 = mp.Process(target=pro2, args=(cond,'p2'))
    p3 = mp.Process(target=pro3, args=(cond,'p3'))
    
    p1.start()
    p2.start()
    time.sleep(3)
    p3.start()
    
    p1.join()
    p2.join()
    p3.join()
    
    
##############
def worker_process(condition,pn):
    condition.acquire()
    condition.wait() ##notifiy를 기다리다가 
    print(f"{pn} it started proceess") #notify가 오면 여기부터 실행
    print(f"{pn} it completed proceess")
    condition
    pass


if __name__=='__main__':
    condition = mp.Condition()
    process1= mp.Process(target = worker_process, args=(condition,))
    process2= mp.Process(target = worker_process, args=(condition,))
    
    process1.start()
    process2.start()
    time.sleep(3)
    condition.acquire()
 #   condition.notify_all()
    condition.notify() ##임의의 프로세스 1개를 깨우고
    condition.release()
    
    process1.join()
    process2.join()