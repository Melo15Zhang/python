#!/usr/bin/python3

class JustCounter:
    __secretCount = 0  # 私有变量
    publicCount = 0  # 公开变量

    def count(self):
        self.__secretCount += 1
        self.publicCount += 1
        print(self.__secretCount)

    def getSecretCount(self):  # 提供对应的public的方法
        return self.__secretCount


counter = JustCounter()
counter.count()
counter.count()
print(counter.publicCount)
# print(counter.__secretCount)  # 报错，实例不能访问私有变量
print(counter.getSecretCount())  # 提供对应的public的方法


# 如果在子类中需要父类的构造方法就需要显示的调用父类的构造方法，或者不重写父类的构造方法。
#
# 子类不重写 __init__，实例化子类时，会自动调用父类定义的 __init__。
# 如果重写了__init__ 时，实例化子类，就不会调用父类已经定义的 __init__
# 如果重写了__init__ 时，要继承父类的构造方法，可以使用 super 关键字：
#
# super(子类，self).__init__(参数1，参数2，....)
# 还有一种经典写法
# 父类名称.__init__(self,参数1，参数2，...)
