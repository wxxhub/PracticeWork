#conding=utf-8   # 中间没有空格
# 2019年2月26日
import Tools
# Python2不能直接支持中文输出

# 【1】 ====注释方式=====
# 单行注释 Ctrl + / 快捷方式
"""
多行注释
"""
'''
多行注释
'''

print("武汉工程大学 智能 Python课堂！！！"); # 分号可加可不加

# 【2】 ====变量====
# python动态属性的语言
# python变量类型在被赋值的时候被定义
a1 = 1;
print(type(a1)); # <class 'int'>
a2 = 1.1;
print(type(a2)); # <class 'float'>
s1 = "武汉工程大学 智能 Python课堂"
print(type(s1)); # <class 'str'>

# 【3】 ====运算符====
"""
+ - * / %
"""
print(4 + 2)
print(4 - 2)
print(4 * 2)
# python中在做两个整数相除，可以获取一个float类型的数据，小数部分为0；
print(4 / 2)
# 两个整数相除，在除不尽的情况下，保留宇哥四舍五入的小数
print(5 / 3)
print(5 % 2)
# 浮点型数据进行相除运算
print(5.0 / 3)
# 双除号在运算中，运算结果只保留整数部分
print(5.0 // 3)
print(5.000 // 3)

# 【4】 ====比较运算符====
"""
< > <= >= !=
"""
print(4 > 2)
print(4 < 2)

"""
java语言中
得分：60 - 80 中等
int a1 = 67;
if (a1 > 60 && a1 < 80){
    ...
}
"""
a3 = 97;
# 条件判断语句：python中支持数据的连续比较
if 60 < a3 < 80 :
    print("成绩中等")
    pass # 占位符
else :
    print("系统无法判断。。。。")
    pass


