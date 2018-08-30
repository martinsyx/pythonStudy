# 闭包
# def curve_pre():
#     # b=20
#     a,b=25,20
#     def curve(x):
#         return b*x*a
#     return curve

# f = curve_pre()
# print(f.__closure__)
# print(f.__closure__[1].cell_contents)
# print(f.__closure__[0].cell_contents)

# def f1():
#     a = 10
#     def f2():
#         a=20
#         print('f2:',a)
#     print('f1:',a)
#     f2()
#     print(a)
# f1()


def traval():
    a=5
    def addis(dist):
        nonlocal a
        a += dist
        return a
    return addis
fn = traval()

print(fn(1))
print(fn(6))