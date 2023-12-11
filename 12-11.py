#5초미만에 쓰고 그러면 정답처리

import time
word = 'cookie'
start_time = time.time()
answer=input("input cookie:")
end_time=time.time()
if (end_time-start_time<5 and answer == word ):
    print("pass")
else:
    print("expired")