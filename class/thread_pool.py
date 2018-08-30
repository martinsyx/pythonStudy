from concurrent.futures import ThreadPoolExecutor,as_completed,wait
import time
def get_html (times):
    time.sleep(times)
    print("get page()")
    return times

executot = ThreadPoolExecutor(max_workers=1)
task1=executot.submit(get_html,(3))
task2=executot.submit(get_html,(2))
# done方法，用于判定某个人物是否完成
time.sleep(5)
print(task1.done())
# print(task2.cancel())
# result方法，阻塞的方法，能够得到返回的结果
print(task1.result())

# 获得已成功的task
urls=[2,3,4]
all_task= [executot.submit(get_html,(url)) for url in urls]
wait(all_task)
# wait(all_task,return_when=FIRST_COM)
print("main")
# for future in as_completed(all_task):
#     data = future.result()
#     print("get {} page success".format(data))

# for data in executot.map(get_html,urls):
#     # data = future.result()
#     print("get {} page success".format(data))