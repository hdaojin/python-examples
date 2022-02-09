"""
类(Class)是用来描述具有相同属性(Attribute)和方法(Method)的对象(Object)的集合。类是创建对象的模版，对象是类的具体实例。
比如，我们可以创建一个类(class)，然后创建该类的实例(instance)，比如，Student类: 
"""


class Student:   # 定义类, 类名首字母大写(驼峰命名), 或者写成class Student(object):
    # 定义类属性(类变量), 类变量在整个实例化的对象中是公用的, 可以在类中直接调用, 不属于任何对象的属性
    number = 0  # 定义类变量
    # 定义学生的属性，初始化方法
    def __init__(self, name, score):  # 初始化构造函数
        self.name = name
        # self.score = score
        self.__score = score  # 私有属性, 只能在类的内部访问
        Student.number += 1  # 类变量自增1

    # 定义方法
    @property  # 利用property装饰器, 可以将方法变成属性调用
    def print_score(self):
        # print('%s: %s' % (self.name, self.score))
        print('%s: %s' % (self.name, self.__score))
    
    @classmethod  # 类方法, 类方法的第一个参数默认是cls, 可以用cls.number访问，使用@classmethod装饰器
    def print_number(cls):  # 类方法, cls为类名
        print('当前学生人数: %s' % cls.number)
    
    @staticmethod  # 静态方法, 不需要传入参数, 使用@staticmethod装饰器
    def print_info():  # 静态方法
        print('这是一个静态方法')

# 实例化对象

student1 = Student('Bob', 88)
student2 = Student('Alice', 99)
student3 = Student('Tim', 77)


# 调用方法
student1.print_score
student2.print_score
# print(student3.__score)  # 私有属性不能在类的外部访问
student3.print_score

# print('Student number: %s' % Student.number) # 访问类变量
# print(student1.__class__.number) # 访问类变量

Student.print_number() # 访问类方法

Student.print_info() # 访问静态方法