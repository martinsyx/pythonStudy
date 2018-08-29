# 线程池 
# from concurrent.futures import threadPoolExecutor
from concurrent.futures import ThreadPoolExecutor
import time
def get_html(times):
    time.sleep(times)
    print("go page {} success".format(times))
    # return times

executor = ThreadPoolExecutor(max_workers=2)

task1=executor.submit(get_html,(3))
task2=executor.submit(get_html,(2))

print(task1.done())
time.sleep(4)
print(task1.done())
