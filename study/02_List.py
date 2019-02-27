
# 序列 - 数据结构
# Python中，最基础的数据结构就是序列
s1 = "武汉工程大学Python课程！"
# 序列中所有的元素都可以根据索引或者下标获取：从0开始；
print(s1[1])
# 在Python中；序列是双向定义：正向从0开始，反向从-1开始；
print(s1[-2])
print(s1[5],s1[-10]);
# 【1】===分片====
s2 = "武汉工程大学Python课程！";
# 序列在进行分片处理的时候：使用索引来访问每一个元素，
# 通过两个元素实现分片效果，中间用:进行分割；[6:12);包前不包后的原则；
print(s2[6:12]);
# 反向分片:第一个参数为开始截取位置，从左往右依次提取；
print(s2[-9:-3]);

# 【2】====集合的分片处理===
N1 = [1,2,3,4,5,6,7,8,9,0]
print(N1[1:5])
print(N1[-3:-1])
print(N1[-3:])
print(N1[:])
print(N1[0:10:2])
# 【3】===序列相加===
print("2019年2月26日"+"武汉工程大学Python实训")
print([1,2,3]+[4,5,6]);
# 两个序列进行相加，必须数据类型一直
# print("2019年2月26日"+[1,2,3,4]);
print("****"*10);
print([1,2,3]*5);
# 【4】===成员资格====
s3 = "武汉工程大学Python课程！";
# 会得到两个数据：True   False
print("Python" in s3)
print("liushuai" in s3)
if "课程" in s3:
    print("文本中存在对于元素。。。")
    pass
# 【5】====在数组中使用in=====
array01 = ["消灭病毒","斗地主","欢乐麻将","跳一跳"]
# 输入语法:获取到一个str类型的数据
name01 = input("请输入游戏名称：\n");
print(type(name01)); #<class 'str'>
if name01 in array01:
    print("在列表中找到了该游戏。。。。");
    pass
# 【6】===序列的长度 最大值，最小值
number01= [1,2,3,4,5,6,7,8,9,0]
# 获取序列长度:len(序列)
print(len(number01))
# 最大值
print(max(number01))
a1 = "abcdfg"
print(max(a1))
print(min(a1))
# 【7】====列表的基本操作====
x = ["狄仁杰","貂蝉","蔡文姬","李白","曹操"];
print(x[0]);
# 重新赋值
x[0] = "后裔"
print(x)
# 删除一个数据
del x[4]
print(x)
# 添加数据
x.append("宫本武藏")
print(x)
x[2]="李白"
print(x)
# 查询元素个数
print(x.count("李白"))
# 序列的扩充:三人组队匹配模式
x1 = ["狄仁杰","貂蝉","蔡文姬"];
print(x1+["曹操","李白"])
# 添加序列
x2 = ["曹操","李白"]
x1.extend(x2)
print(x1)
del x1[0:2];
print(x1)
# insert插入
array02 = ["消灭病毒","斗地主","欢乐麻将","跳一跳","斗地主"]
array02.insert(1,"消灭星星");
print(array02);
# 根据下标或索引删除一个元素
array02.pop(1)
print(array02)
# 根据元素名称删除元素：remove函数没有返回数据-只会删除第一匹配到的元素；
print(array02.remove("斗地主"))
print(array02)


