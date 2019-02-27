# 4 比较运算符
print(4>2)
print(4<2)
print(4<=2)
#条件判断语句
a3=67;
if 60<a3<80:
  print("成绩中等")
  pass #占位符
else
  print("其他")
  
 
# ===序列-数据结构===

s1="witPython课堂!";
#在Python中：序列的双向：正从0开始，反从-1开始；
print(s1[2])
print(s1[-1])

# ====分片=====
s2="witPython课堂!";
print(s2[6:10])
通过两个元素实现分片效果，中间用:进行分割；[5:10)


#【2】====集合分片处理=====
N1=[1,2,3,4,5,6,7]
print(N1[1:5])
print(N1[-3:-1])
print(N1[0:10:2])


#【3】  序列相加
print("2019年2月26日+witPython课堂");
#两个序列相加，必须数据类型一致
print([1,2,3]+[4,5,6])

#【4】======成员资格============
s3 ="witPython课堂!";
# 会得到两个数据： true false
print("Python"in s3)
print("liiijin"in s3)

#【5】 =========在数组中使用in========
array01=["消灭病毒","弹珠王者","斗地主"]
name01=input("input game name: \n");
print(type(name01));   #<class str>
if name01 in array01:
print("找到该游戏。。。。。")


#【6】==序列长度  max min
number1=[1,2,3,77,9,87,6,0]
#len(序列):获取序列长度
print(len(number1))
print(max(number1))


#【7】 ===列表的基本操作====

n=["wxx","chq","zyh","hhc","lsf"];
print(n[0])
#重新赋值
n[1] ="dfh"
print(n)
#删除数据
del n[3]
print(n)
#添加数据
n.append("sft")
print(n)
#查询数据个数
print(n.count("chq")

#序列扩充
n1=([],[],[])
print(n1+"")

#插入
insert
array01.insert(2,"跳一跳")#2表示插入的位置




