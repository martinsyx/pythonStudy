import threading

class XiaoAI(threading.Thread):
    def __init__(self,lock):
        super().__init__(name="ai")
        self.lock = lock

    def run(self):
        self.lock.acquire()
        print("{}: hi".format(self.name))
        self.lock.release()

        self.lock.acquire()
        print("{}: hi".format(self.name))
        self.lock.release()

class TianMao(threading.Thread):
    def __init__(self,lock):
        super().__init__(name="miao")
        self.lock =lock
    def run(self):
        self.lock.acquire()
        print("{} :ai sang".format(self.name))
        self.lock.release()

        self.lock.acquire()
        print("{} :ai sang2".format(self.name))
        self.lock.release()

if __name__ == "__main__":

    lock =threading.Lock()
    xiaoai = XiaoAI(lock)
    miao =TianMao(lock)

    miao.start()
    xiaoai.start()
