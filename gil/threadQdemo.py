from Queue import Queue
import threading
import time

def get_Datail_html(queue):
    while True:

        url=queue.get()
        print ("html start")
        time.sleep(2)
        print('html end')

def get_Datail_url(queue):
    while True:
        for i in range(20):
            queue.put("http://projectsedu.com/{id}".format(id=i))
            print('utl end')

if __name__ == "__main__":
    detail_url_queue = Queue(maxsize=100)
    thread_detail_url = threading.Thread(target=get_Datail_url,args=(detail_url_queue))
    for i in range(10):
        html_thread= threading.Thread(target=get_Datail_html,args=(detail_url_queue))
        html_thread.start()

    # thread1.join()
    # thread2.join()
    detail_url_queue.task_done()
    detail_url_queue.join()


    print("last time :{}".format(time.time()-start_time))