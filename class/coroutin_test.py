# 协程 有多个入口的函数，可以暂停的函数（可以暂停的地方传入值），
# from itertools import chain



# def gen_func():
#     html = yield "http://www.baidu.com"
#     # print(html)
#     yield 2
#     yield 3
#     return 'martin'
# #生成器不止产处值，还可以接收值
# if __name__ == "__main__":
#     gen =gen_func()
#     # url = next(gen)
#     # print(url)
#     # gen.send('my')
#     print(next(gen))
#     print(next(gen))
#     print(next(gen))


# my_list = [11,22,33]
# my_dict = {
#     "mt1":"www.baidu.com",
#     "mt2":"www.google.com"
# }

# for value in chain(my_list,my_dict):
#     print(value)

# def g1(iterable):
#     yield iterable



# for value in g1(range(10)):
#     print(value)
# for value in g2(range(10)):
#     print(value)

def g1(gen):
    yield from gen
def main():
    g = g1()
    g.sned(None)
def g2(iterable):
    yield from iterable