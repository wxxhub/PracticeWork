
# 【1】===创建类和使用类====
# 写法一
class Person_01:
    name = "Person_01"
    pass
class Person_02():
    name = "Person_02"
    pass
class Person_03(object):
    name = "Person_03"
    pass
# 测试-实例化：Java语法中 - Person_01 person = new Person();
person_01 = Person_01();
print(person_01.name);
person_02 = Person_02();
print(person_02.name);
person_03 = Person_03();
print(person_03.name);
# 【2】===类的构造函数=====
class Person_04(object):
    # name = ""
    # age = 10;
    # 构造函数的写法
    # self:表示类的本身 - Person_04:
    # 构造函数用用self.属性名 - 全局变量
    def __init__(self,name,age,height,weight,money):
        self.name = name;
        self.age = age;
        self.height = height;
        self.weight = weight;
        self.money = money;
        pass
    # 函数
    def SetName(self,name):
        self.name = name;
        pass
    def GetName(self):
        return self.name;
        pass

    pass
# 带构造函数类的实例化
person_04 = Person_04("宫本武藏",18,170,70,100);
print(person_04.name);
print(person_04.money);
# 调用set,get函数
person_04.SetName("李白");
print("返回的名称为："+person_04.GetName())





