import multiprocessing as mp

mp.freeze_support
import time

def pro1(v,pn):
    #print(f"Value객체의 초기값: {v}")
    print(f"{pn}: Value객체의 초기 값: {v.value}")
    pass

def pro2(v,pn):
    #time.sleep(3)
    pass

mn= mp.Manager()

if __name__=='__main__':
    value = mp.Value('i',0)
    ## 데이터 공유를 위해 value객체를 생성. i: 정수, 초기값: 0
    p1= mp.Process(target=pro1,args=(value,'p1'))
    p2= mp.Process(target=pro2,args=(value,'p2'))

p1.start()
p2.start()

