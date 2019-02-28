
# 【赋值操作】
# 1.常规
a = 10;
b = "武汉工程大学"
# 2.序列解包赋值
x,y,z = "上路","下路","中单";
print(x,y,z)
x,z = z,x;
print(x,y,z)
# 【1】====条件语句====
# if elif ... else
# name = input("请输入要查询的英雄:")
# # startswith：从开始0下标的位置进行匹配，直至匹配到对应（狄仁）的元素。
# if name.startswith("狄仁"):
#     print("您要查询的英雄为狄仁杰！！")
#     pass
# elif name.startswith("甄"):
#     pass
# else:
#     pass2

# 嵌套if语句
print("===========嵌套if语句===========")
name = int(input("1.狄仁杰 \n2.曹操 \n3.后羿\n请输入英雄编号：")) #str
# (int)值
print(type(name))
if name == 1:
    print("您已经选定英雄：%d\n 请选择行走路线:\n1.上路 \n2.下路 \n3.中单"%name)
    num = int(input("请输入编号:"))
    if num == 1:  
        print("您选择e英雄：%d,路线选择%d"%(name,num))
        pass
    elif num == 2:
        print("您选择英雄：%s,路线选择%d"%(name,num))
        pass
    else:
        print("您选择英雄：%s,路线选择%d"%(name,num))
        pass
elif name == 2:
    if num == 1: 
        print("您选择英雄：%s,路线选择%d"%(name,num))
        pass
    elif num == 2:
        print("您选择英雄：%s,路线选择%d"%(name,num))
        pass
    else:
        print("您选择英雄：%s,路线选择%d"%(name,num))
        pass
    pass
else:
    if num == 1: 
        print("您选择英雄：%s,路线选择%d"%(name,num))
        pass
    elif num == 2:
        print("您选择英雄：%s,路线选择%d"%(name,num))
        pass
    else:
        print("您选择英雄：%s,路线选择%d"%(name,num))
        pass
pass
# 【2】===循环语句===
print("=======while循环输出语句=========")
array_01 = ["1.消灭病毒","2.斗地主","3.欢乐麻将","4.跳一跳","5.泡泡大作战"];
print(array_01)
x = 0;
while x<len(array_01):
    print(array_01[x])
    x+=1;
    pass
# for循环
"""
for(int i=0;i<5;i++){

}
"""
print("======for循环-in=========")
array_01 = ["1.消灭病毒","2.斗地主","3.欢乐麻将","4.跳一跳","5.泡泡大作战"];
print("1.消灭病毒" in array_01)
for name in array_01:
    print(name)
    pass
# 涉及到数字的循环
print("======for循环-数字=====")
for number in range(0,len(array_01)):
    print(array_01[number])
    s1 = array_01[number]; #"1.消灭病毒"
    for sm in s1:
        print(sm)
        pass
    pass