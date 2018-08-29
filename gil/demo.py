import threading
import time
start_time=time.time()
def get_Datail_hrml():
    print ("html start")
    time.sleep(2)
    print("html end :{}".format(time.time()-start_time))
    # print('html end')

def get_Datail_utl():
    print("utl start :{}".format(time.time()-start_time))
    time.sleep(2)
    # print('utl end')
    print("utl end :{}".format(time.time()-start_time))

start_time=time.time()
get_Datail_hrml()
get_Datail_utl()

print("last time :{}".format(time.time()-start_time))