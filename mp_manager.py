##### Manager 클래스로 객체 공유하기.

import multiprocessing as mp

mp.freeze_support
import time

def pro1(ml,pn):
    #print(f"Value객체의 초기값: {v}")
    ml.append('p1')
    print(f"{pn}현재 리스트의 값 :{ml}")


def pro2(ml,pn):
    #time.sleep(3)
    ml.append('p2')
    print(f"{pn}현재 리스트의 값을 추가했습니다. :{ml}")
  



if __name__=='__main__':
    mn=mp.Manager()
    manager_list=mn.list() ## 빈 리스트 생성[]
    #manager_list = mn.dict() #dict type으로 넘길수 도 있다.
    #빈 딕셔너리 생성 {}
    p1= mp.Process(target=pro1,args=(mn,'p1'))
    p2= mp.Process(target=pro2,args=(mn,'p2'))

    

p1.start()
p2.start()
p1.join()
p2.join()
