## object sharing between processes : Queue()class
## input data from p1, program that read data from p2 and print

from multiprocessing import Queue, Process
import time


# def pro1(q):
#     print(f"")
#     #input data to q
#     for i in range(100):
#         q.put(i) ##put(): Method for entering data
#         time.sleep(1)
        
# def pro2(q):
#     items = [] ## List to store get() data
#     while True:
#         item = q.get() ##bring data 
#         items.append(item)
#         print(f"p2:q객체에서 {item}를 가져왔습니다.")
#         print(f"현재 q에 저장된 값은 {items}입니다.")
        
# #maincode part
# if __name__ =='__main__':
#     queue=Queue() ## after create obj of queue class, store to queue reference variable 
#     p1=Process(target=pro1,args=(queue,))
#     p2=Process(target=pro2,args=(queue,))
    
#     p1.start()
#     p2.start()
    
#     p1.join()
#     p2.join()
