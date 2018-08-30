# 多cpu的操作 ，用多进程操作，对于io操作，使用多线程编程。
# 进程切换的代价高于线程，
from concurrent.futures import ThreadPoolExecutor,as_completed
from concurrent.futures import ProcessPoolExecutor
import time
def fib(n):
    if n<=2:
        return 1
    return fib(n-1)+fib(n-2)



# 多线程编程
# with ThreadPoolExecutor(3) as executor:
#     all_task =[executor.submit(fib,(num))for num in range(25,40)]
#     start_time = time.time()
#     for future in as_completed(all_task):
#         data=future.result()
#         print('exe result: {}'.format(data))

#     print('last time is : {}'.format(time.time()-start_time))
# print(fib(40))
# 多进程编程
# if __name__ == "__main__":
#     with ProcessPoolExecutor(3) as executor:
#         all_task =[executor.submit(fib,(num))for num in range(25,40)]
#         start_time = time.time()
#         for future in as_completed(all_task):
#             data=future.result()
#             print('exe result: {}'.format(data))

#         print('last time is : {}'.format(time.time()-start_time))


def random_sleep(n):
    time.sleep(n)
    return n

# 多线程编程
with ThreadPoolExecutor(3) as executor:
    all_task =[executor.submit(random_sleep,(num))for num in [1]*60]
    start_time = time.time()
    for future in as_completed(all_task):
        data=future.result()
        print('exe result: {}'.format(data))

    print('last time is : {}'.format(time.time()-start_time))

# 多进程编程
# if __name__ == "__main__":
#     with ProcessPoolExecutor(3) as executor:
#         all_task =[executor.submit(random_sleep,(num))for num in [1]*60]
#         start_time = time.time()
#         for future in as_completed(all_task):
#             data=future.result()
#             print('exe result: {}'.format(data))

#         print('last time is : {}'.format(time.time()-start_time))

