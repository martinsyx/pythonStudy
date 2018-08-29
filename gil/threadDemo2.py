import threading
import time

class GetDetailHTML(threading.Thread):
    # def __init__(self,name):

    def run(self):
            print ("html start")
            time.sleep(2)
            print('html end')

class GetDetailURL(threading.Thread):
    def run(self):
            print ("url start")
            time.sleep(2)
            print('url end')


if __name__ == "__main__":

    thread1 = GetDetailHTML()
    thread2 = GetDetailURL()
    # thread1.setDaemon(True)
    # thread2.setDaemon(True)
    start_time  = time.time()
    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()


    print("last time :{}".format(time.time()-start_time))