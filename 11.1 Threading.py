import time
from threading import Thread, Lock


class SimpleThread(Thread):
    key = Lock()
    def __init__(self, name, delay):
        super().__init__()
        self.name = name
        self.delay = delay

    def run(self):
        for i in range(0, 6):
            with SimpleThread.key:
                print(self.name, i)
            time.sleep(self.delay)
    
t1 = SimpleThread('Peter', 3)
t1.start()
t2 = SimpleThread('Erik', 3)
t2.start()

t1.join()
t2.join()

