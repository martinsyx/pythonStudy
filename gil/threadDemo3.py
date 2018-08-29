import threading
import time
detail_url_list=[]
def get_Datail_html(url):
    global detail_url_list
    while True:
        if len(detail_url_list):
            url=detail_url_list.pop()
            print ("html start")
            time.sleep(2)
            print('html end')

def get_Datail_url(url):
    global detail_url_list
    while True:
        for i in range(20):
            detail_url_list.append("http://projectsedu.com/{id}".format(id=i))
            print('utl end')

if __name__ == "__main__":
    thread_detail_url = threading.Thread(target=get_Datail_url)
    for i in range(10):
        html_thread= threading.Thread(target=get_Datail_html)
        html_thread.start()

    # thread1 = threading.Thread(target=get_Datail_hrml,args=("",))
    # thread2 = threading.Thread(target=get_Datail_utl,args=("",))
    # thread1.setDaemon(True)
    # thread2.setDaemon(True)
    # start_time  = time.time()
    # thread1.start()
    # thread2.start()

    thread1.join()
    thread2.join()


    print("last time :{}".format(time.time()-start_time))