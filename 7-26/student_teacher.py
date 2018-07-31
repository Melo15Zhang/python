from collections import Counter
import sys


class Person(object):
    """
    返回具有给定名称的 Person 对象
    """

    def __init__(self, name):
        self.name = name

    def get_details(self):
        """
        返回包含人名的字符串
        """
        return self.name

    def get_grade(self, point):
        return ""


class Student(Person):
    """
    返回 Student 对象，采用 name, branch, year 3 个参数
    """

    def __init__(self, name, branch, year):
        Person.__init__(self, name)
        self.branch = branch
        self.year = year

    def get_details(self):
        """
        返回包含学生具体信息的字符串
        """
        return "{} studies {} and is in {} year.".format(self.name, self.branch, self.year)

    def get_grade(self, point):
        str = Counter(point)
        passed = 0
        failed = 0
        for x,y in str.most_common(4):
            if x in ['D']:
                failed += y
            else:
                passed += y
        print('Pass: {}, Fail: {}'.format(passed, failed), end="")


class Teacher(Person):
    """
    返回 Teacher 对象，采用字符串列表作为参数
    """
    def __init__(self, name, papers):
        Person.__init__(self, name)
        self.papers = papers

    def get_details(self):
        return "{} teaches {}".format(self.name, ','.join(self.papers))


    def get_grade(self, point):
        str = Counter(point)
        temp = []
        for x,y in str.most_common(4):
            temp.append('{}: {}'.format(x, y))

        print(",".join(temp), end="")


if __name__ == '__main__':
    point = sys.argv[2]
    if sys.argv[1] == 'student':
        student1 = Student('student', 'CSE', 2005)
        student1.get_grade(point)
    elif sys.argv[1] == 'teacher':
        teacher1 = Teacher('Prashad', ['C', 'C++'])
        teacher1.get_grade(point)
    else:
        print("argv error")