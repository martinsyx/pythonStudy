# 匿名函数
# def add(x,y):
#     return x+y
 
# f = lambda x,y :x+y
# print(f(1,2))t
lists =[1,2,3,4,5,6,7,8]
def square(x):
    return x*x
r = map(square,lists)
# print(list(r))
p= map(lambda x:x*x,lists)
# print(list(p))

list_y = [1,2,4,5,6,7,8,9]
# 尝试下数据不相等list_y = [1,2,4,5]
q = map(lambda x,y :x+y,lists ,list_y )
print(list(q))