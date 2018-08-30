import time
from multiprocessing import Process,Queue,Pool,Manager,Pipe

# def producer(que):
#     que.put("a")
#     time.sleep(2)

# def consumer(que):
#     time.sleep(2)
#     data = que.get()
#     print(data)

# if __name__ == "__main__":
#     que = Queue(10)
#     my_producer = Process(target=producer,args=(que,))
#     my_consumer = Process(target=consumer,args=(que,))
#     my_producer.start()
#     my_consumer.start()
#     my_producer.join()
#     my_consumer.join()
# 共享全局变量通信
# def producer(a):
#     # que.put("a")
#     a+=1
#     time.sleep(2)

# def consumer(a):
#     time.sleep(2)
#     print(a)

# if __name__ == "__main__":
#     # que = Queue(10)
#     a=1
#     my_producer = Process(target=producer,args=(a,))
#     my_consumer = Process(target=consumer,args=(a,))
#     my_producer.start()
#     my_consumer.start()
#     my_producer.join()
#     my_consumer.join()

 # multiprocessing中的queue不能用于pool进程池

# def producer(que):
#     que.put("a")
#     time.sleep(2)

# def consumer(que):
#     time.sleep(2)
#     data = que.get()
#     print(data)

# if __name__ == "__main__":
#     que = Manager().Queue(10)
#     # que = Queue(10)
#     pool  = Pool(2)
#     pool.apply_async(producer,args=(que,))
#     pool.apply_async(consumer,args=(que,))
#     pool.close()
#     pool.join()


#  通过pipe进行进程间通信
# Pipe的性能高于queue
# def producer(pip):
#     pip.send('ppp')

# def consumer(pip):
#    print(pip.recv())

# if __name__ == "__main__":
#     que = Manager().Queue(10)
#     # pipe只能适用于两个进程
#     receive_pipe,send_pipe=Pipe()
#     my_producer = Process(target=producer,args=(receive_pipe,))
#     my_consumer = Process(target=consumer,args=(send_pipe,))
#     my_producer.start()
#     my_consumer.start()
#     my_producer.join()
#     my_consumer.join()

def add_data(p_dict,key,value):
    p_dict[key] = value
if __name__ == "__main__":
    process_dict = Manager().dict()
    first_process=Process(target=add_data,args=(process_dict,'hello',':'))
    second_process=Process(target=add_data,args=(process_dict,'word','!'))
    first_process.start()
    second_process.start()
    first_process.join()
    second_process.join()
    print(process_dict)