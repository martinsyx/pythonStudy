# 并发是指一个时间段内，有多个程序在同一个cpu上运行，但是任意时刻只有一个程序在cpu上运行
# 并行是指任意时刻点上，有多个程序同时运行在多个cpu上
# 组赛和非阻塞是对函数的调用
# 阻塞是指调用函数时候线程被挂起
# 非阻塞是指调用函数时候线程不会被挂起，而是立即返回

# Unix下的五种I/O模型
# 阻塞式I/O
# 非阻塞式I/O
# I/O复用
# 信号驱动I/O
# 异步I/O（POSIX的aio_系列函数）

# I/O多路复用
# 通过非阻塞实现HTTP请求


async def downloader(url):
    return "hello"

async def download_url(url):
    html = await downloader(url)
    return html

if __name__ =="__main__":
    coro = download_url('www.baidu.com')
    coro.send(None)
    
