import dis
from  threading import Lock

lock = Lock()

# def add(a):
#     a = a+1
#     return a

# print(dis.dis(add))

total = 0

def add():
    global total 
    global lock
    for i in range(1000000):
        lock.acquire()
        total +=1
        lock.release()

def desc():
    global total
    global lock
    for i in range(1000000):
        lock.acquire()
        total -=1
        lock.release()

import threading
thread1 = threading.Thread(target=add)
thread2 = threading.Thread(target=desc)
# thread3 = threading.Thread(target=desc)
thread1.start()
thread2.start()

thread1.join()
thread2.join()

print(total)

