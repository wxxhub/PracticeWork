
# 导入包
from Case01.多继承.Father import Father_01
from Case01.多继承.Mother import Mother_01

# 子类继承父类
# 多继承时：只需要按照对应顺序依次添加，用逗号分隔；
# 子类继承多个父类的时候，构造函数会继承靠近子类的父类
class Child_01(Mother_01,Father_01):
    # Child_01  Mother_01  Father_01
    # 重新构造函数
    def __init__(self,money,managemoney):
        super(Child_01,self).__init__(managemoney);
        super(Mother_01,self).__init__(money);
        pass

    pass

# 实例化W
child_01 = Child_01(1000,200)
# 子类调用母亲的属性
print("调用母亲的属性：",child_01.managemoney);
print("调用父亲的属性：",child_01.money)
# 功能可以继承
child_01.playChild()
child_01.Shopping()