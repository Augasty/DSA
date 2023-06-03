from threading import * 
import time

lock = Lock()
count = 0

def task():
    lock.acquire()
    global count
    for i in range(10000000):
        count += 1
    lock.release()

if __name__=='__main__':
    t1 = Thread(target=task)
    t2 = Thread(target=task)

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print(count)
