#THREAD
"""
import threading

from threading import Thread
import time
class Mythread(threading.Thread):
    def __init__(self,i):
        threading.Thread.__init__(self)
        self.h=i

    def run(self):
        time.sleep(5)
        print("value send",self.h)
thread1=Mythread(1)
thread1.start()
thread2 = Mythread(2)
thread2.start()


#thread count
import threading

from threading import Thread
import time
class Mythread(threading.Thread):
    def __init__(self,i):
        threading.Thread.__init__(self)
        self.h=i
    def run(self):
        print("no. is",self.h)
        time.sleep(1)

for i in range(10):
    thread1=Mythread(i)
    thread1.start()

    print("active threads are", threading.active_count())

#thread join
import threading

from threading import Thread
import time
class Mythread(threading.Thread):
    def __init__(self,i):
        threading.Thread.__init__(self)
        self.h=i

    def run(self):
        time.sleep(5)
        print("value send",self.h)
thread1=Mythread(1)
thread1.start()
thread1.join()
thread2 = Mythread(2)
thread2.start()
thread2.join()
"""

def sleepMe(i)
    print("thraed is going to sleep for 5 sec ")
    time.sleep(5)
    print("thraed is awake now"$i)
for i in range(10):
    th=Thread(target=sleep,args=(i,))


    """"""
    time.sleepcounter
    """"""