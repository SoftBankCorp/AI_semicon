def pro1(sq):
    for i in range(10):
        sq.put(i)
        print(f"p1:simpleQueue 객체에 {i}를 담았습니다.")
        time.sleep(0.5)
        
def pro2(sq):
    items = []
    while True:
        item = sq.get()
        if item is None:
            print("p2:SimpleQueue객체의 모든 내용을 가져왔습니다.끝")
            break
        print(f"p2:simpleQueue의 값: {item}")
        items.append(item)
    print(f"p2:리스트 담은 값은 {item}입니다.")
    ##객체를 공유하려면 객체를 공유하는 클래스를 ..
    #함수들에게 그 객체를 넘겨주어 그 같은애를 공유할 수있도록한다.
    #그러면 put과 get을 통해 주고 받을 수 있음.
    
    #put이  blocking 될 때는 언제면, 
    #파이썬은 데이터가 동적으로 할당된다.
    #메모리를 integer type으로 .~ 이는데
    #공간에 대이터가 꽉차면 더 넣을 수 가 없어 blocking한다.
    #queue객체는 선입선출이기.  get메소드는 값이 안오면 값이 올때까지 기다리면서 blocking한다.
    ###따라서 데이터객체에다가 none이란 객체를 넣고, 그값이 none이면 멈춘다.
    #이렇게 하여 get메소드가 계속 대기타지 않도록 만들어줌 
    #value객체 . - >     
        
if __name__ == '__main__':
    sq= SimpleQueue()
    p1= Process(target=pro1, args=(sq,))
    p2= Process(target=pro2, args=(sq,))
    
    p1.start()
    p2.start()
    p1.join()
    sq.put(None) 
    ##get()메소드는 데이터가 들어올 때 까지 대기상태에 있으므로
    ##대기를 멈추게 하기 위해서 put()메서드를 통해서 None이라는 값을 
    ##SimpleQueue()에 전달을 하고 p2에서는 값을 확인하는 작업을 통해서
    ##데이터의 입력의 끝의 여부를 확인할 수 있도록 만들어 줌
    
    #none을 넘겨줘서 끝을 표시해줌
    #none을 simple queue 객체에 넘겨줌
    p2.join() #
