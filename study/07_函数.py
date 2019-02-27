
# 【1】====创建函数=====
def func(a):
    print("函数被调用。。。。。%s"%a)
    pass
func("2019年2月27日");#调用已经写好的函数
#
print("=====传入两个参数======")
def func1(a,b):
    print("%d函数被调用。。。。。%s"%(b,a))
    pass
func1("2019年2月27日",1000);#调用已经写好的函数

print("=====带返回值======")
def func2(a,b):
    c = a+b;
    return c
    pass
print("返回的数据为："+str(func2(200,1000)));#调用已经写好的函数
