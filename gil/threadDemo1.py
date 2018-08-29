import threading
import time

def get_Datail_hrml(url):
    print ("html start")
    time.sleep(2)
    print('html end')

def get_Datail_utl(url):
    print ("utl start")
    time.sleep(2)
    print('utl end')

if __name__ == "__main__":

    thread1 = threading.Thread(target=get_Datail_hrml,args=("",))
    thread2 = threading.Thread(target=get_Datail_utl,args=("",))
    thread1.setDaemon(True)
    thread2.setDaemon(True)
    start_time  = time.time()
    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()


    print("last time :{}".format(time.time()-start_time))