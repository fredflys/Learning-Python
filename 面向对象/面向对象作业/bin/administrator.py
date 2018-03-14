import time
import pickle
import random
from lib import modules
from config import settings
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)))


def main():
    inp = input('1.Admin log-in\n2.Admin register>>>')
    user = input('Please enter your username:')
    pwd = input('Please enter your password:')
    if inp == '1':
       ret = login(user,pwd)
       if ret == 1:
           print('Invalid passowrd.')
       elif ret == 0:
           print('User does not exist.')
    elif inp == '2':
        register(user,pwd)

def login(user,pwd):
    if os.path.exists(user):
        admin_obj = pickle.load(ope(user,'rb'))
        if admin_obj.login(user,pwd):
            print('Logon success.')
            while True:
                sel = input('1.Create a teacher.\n2.Create a course')
                if sel == '1':
                    create_teacher(admin_obj)
                elif sel == '2':
                        create_course(admin_obj)
                    else:
                        break
                    else:
                        return 1
        else:
            return 0
def register(user,pwd):
     admin_obj = modules.Admin()
     admin_obj.register(user,pwd)

def create_teacher(admin_obj):
    teacher_list = []
    while True:
        name = input('Please enter teacher\'s name:(Q for quit)')
        if name == 'q':
            break
        age = input('Please enter teacher\'s age:')
        obj = modules.Teacher(name,age,admin_obj)
        teacher_list.append[obj]
    if os.path.exists(settings.TEACHER_DB_DIR):
        exists_list = pickle.load(open(settings.TEACHER_DB_DIR,'rb'))
        teacher_list.extend(exists_list)
    pickle.dump(teacher_list,open(settings.TEACHER_DB_DIR,'wb'))

def create_course(admin_obj):
    teacher_list = pickle.load(open(settings.TEACHER_DB_DIR,'rb'))
    for num,item in enumerate(teacher_list,1):
        print(num,item.name,item.age,item.create_time,item.create_admin.username)
    course_list = []
    while True:
        name = input('Please enter course name: ')
        cost = input('Please enter course cost: ')
        num = input('Please select a teacher(enter the number): ')
        obj = modules.Course(name,cost,teacher_list[int(num)-1],admin_obj)
        course_list.append(obj)

    if os.path.exists(settings.COURSE_DB_DIR):
        exists_list = pickle.load(open(settings.COURSE_DB_DIR,'rb'))
        course_list.extend(exists_list)
    pickle.dump(teacher_list,open(settings.COURSE_DB_DIR,'wb'))

if __name__ = '__main__':
    main()
