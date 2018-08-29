# 信号量 控制进入数量的锁

# 文件读写，写一般只是用于一个线程的写，读可以允许有多个dd
import threading
import time
class UrlProducer(threading.Thread):
    def __init__(self,sem):
        super().__init__()
        self.sem = sem
        

    def run(self):
        for i in range(20):
            self.sem.acquire()
            
            html_thread = htmlSpider("http://www.google.com?{}".format(i),self.sem )
            html_thread.start()

class htmlSpider(threading.Thread):
    def __init__(self,url,sem):
        super().__init__()
        self.sem = sem
        self.url = url
    def run(self):
        time.sleep(2)
        print('go html  test success!')
        self.sem.release()

if __name__ =="__main__":
    sem  = threading.Semaphore(3)
    url_produce = UrlProducer(sem)
    url_produce.start()
