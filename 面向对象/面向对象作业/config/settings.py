import os
#找到settings.py的路径，向上再找一层
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
BASE_ADMIN_DIR = os.path.join(BASE_DIR,'db','admin')
TEACHER_DB_DIR = os.path.join(BASE_DIR,'db','teacher_list')
COURSE_DB_DIR = os.path.join(BASE_DIR,'db','course_list')

