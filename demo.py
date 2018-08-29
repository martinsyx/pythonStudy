
a = [['a','b','c'],[1,2,3]]

# for x in a:
#     for y in x:
#         if y == 'b':
#             break
#         print(y)
# else :
#     print('is end')

# for i in range(100,10,-2):
#     print(i,end=" | ")

a = [1,2,3,4,5,6,7,8,9]

for i in range(0,len(a),2):
    print(a[i],end = "| ")

b = a[0:len(a):2]
print(b)