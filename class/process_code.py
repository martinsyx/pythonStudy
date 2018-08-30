import os
import time
# fork 会创建子进程 只用于linux/unix
pid = os.fork()
if pid == 0:
    print('子进程{}，父进程是{}'.format(os.getpid(),os.getppid()))
else:
    print('我是父进程：{}'.format(pdi))
time.sleep(2)