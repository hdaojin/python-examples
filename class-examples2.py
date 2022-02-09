"""
类的继承: 子类可以继承父类的所有属性和方法
"""

class SchoolMember:
    """
    一个简单的类，用于存储学校成员的信息
    """
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def tell(self):
        """
        定义方法
        """
        print('%s: %s' % (self.name, self.age), end=' ')

class Teacher(SchoolMember):
    """
    定义Teacher类，继承SchoolMember类
    """
    def __init__(self, name, age, salary):
        SchoolMember.__init__(self, name, age)  # 调用父类的构造函数, 必须放在子类的构造函数的第一行, 进行初始化
        self.salary = salary

    def tell(self):   # 重写父类的方法
        SchoolMember.tell(self)
        print('salary: %s' % self.salary)

class Student(SchoolMember):
    """
    定义Student类，继承SchoolMember类
    """
    def __init__(self, name, age, marks):
        super().__init__(name, age)  # 调用父类的构造函数, 必须放在子类的构造函数的第一行, 进行初始化
        self.marks = marks

    def tell(self):   # 重写父类的方法
        super().tell()  # 等同于SchoolMember.tell(self)
        print('marks: %s' % self.marks)


teacher1 = Teacher('Bob', 40, 30000)
teacher2 = Teacher('Alice', 30, 20000)

student1 = Student('Tim', 20, 90)
student2 = Student('Jack', 18, 80)


teacher1.tell()
teacher2.tell()

student1.tell()
student2.tell()

