
import threading
from threading import Condition 
# 条件变量 用于复杂的线程间同步

class XiaoAi(threading.Thread):
    def __init__(self,cond):
        super().__init__(name="xiaoAi")
        self.cond= cond

    def run(self):
        with self.cond:
            self.cond.wait()
            print("{}:zai".format(self.name))
            self.cond.notify()

            self.cond.wait()
            print("{}:haihaihai".format(self.name))
            self.cond.notify()

class Tianmao(threading.Thread):
    def __init__(self,cond):
        super().__init__(name="tianMao")
        self.cond= cond

    def run(self):
        with self.cond:
            print("{}:xiaoAi".format(self.name))
            self.cond.notify()
            self.cond.wait()

            print("{}:womenlaihai".format(self.name))
            self.cond.notify()
            self.cond.wait()



        
if __name__ == "__main__":
    cond = threading.Condition()
    xiaoai = XiaoAi(cond)
    tianmao = Tianmao(cond)
    xiaoai.start()
    tianmao.start()




