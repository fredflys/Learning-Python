#-*- coding:utf-8 -*-
'''
选课系统
    管理员
        创建老师：姓名、性别、年龄、职称、资产（对应课时费）
        创建课程：名称、上课时间、课时费、关联老师
        使用pickle保存在文件中
    学生
        学生：用户名、密码、性命、性别、年龄、选课列表（默认为空）、上课记录
        选课：1.列举所有课程
              2.选课（保存在每个学生的选课列表中）
              3.上课（获取课程的返回值，保存在上课记录中）
'''
import pickle

class Teacher:
    def __init__(self,name,age):
        initial_list = []
        self.name = name
        self.age = age
        # 只有自己可以看到，用成员修饰符
        self.__asset = 0
        self_dict = {'name':self.name,'age':self.age,'asset':self.__asset}
        with open(r'D:\Learning\python files\teachers','ab+') as f:
            try:
                teacher_list_obj = pickle.load(f)
            #如果文件不存在，pickle.load方法会产生EOFerror，捕获之，并新建老师列表
            except EOFError as e:
                print(e)
                teacher_list_obj = initial_list
                teacher_list_obj.append(self_dict)
                pickle.dump(teacher_list_obj,f)
            else:
                if self_dict in teacher_list_obj:
                    print('This teacher exists in the list.No need to create.')
                else:
                    teacher_list_obj.append(self.dict)
                    f.truncate()
                    pickle.dump(teacher_list_obj,f)
    @staticmethod
    def display():
         with open(r'D:\Learning\python files\teachers','rb') as f:
                teacher_list_obj = pickle.load(f)
                print(teacher_list_obj)


class Course:
    def __init__(self,name,fee,teacher_obj):
        self.name = name
        self.fee = fee
        self.teacher_obj = teacher_obj
        with open('D:\Learning\python files\courses','a+'):
            pickle.dump(self,'D:\Learning\python files\courses')

    def display(self):
        with open('D:\Learning\python files\courses','rb') as f:
            for line in f:
               course_obj = pickle.load('D:\Learning\python files\courses')


class Student:
    def __init__(self,name):
        self.name = name

    def register(self):
        pass

    def logon(self):
        pass

    def select_courses(self):
        pass


Teacher('John',26)
Teacher('John',26)
