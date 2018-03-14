''''''
def myfilter(func,seq):
      result = []
      for i in seq:
            if func(i):
                  result.append(i)
            else:
                  pass
      return result

def com(num):
      if num > 100:
            return True
      else:
            return False
 #r = myfilter(com,[12,155,199,200,38,98,18,75,17])
 #print (r)


x = lambda i : i + 100
def mymap(fun,arg):
      result = []
      for i in arg:
            result.append(fun(i))
      return result
#############################################
#用户登录
#user$password
def user_input():
      usn = input('User name:')
      pwd = input('Password:')
      return usn,pwd

def if_user_exists(usn):
      #逐行查找，如存在，返回真
      with open('C:\Python36\TEST\db','r',encoding='utf-8') as f:
            for line in f:
                  line = line.strip()
                  line_list = line.split('$')
                  if line_list[0] == usn:
                        return True
      return False

def login_if():

#用于登陆的用户名和密码验证
#:param usn:登录名
#:param pwd:密码
#:return True,登陆成功 False,登陆失败
      usn,pwd = user_input()
      with open('C:\Python36\TEST\db','r',encoding='utf-8') as user_db:
            for line in user_db:
                  line = line.strip()
                  line_list = line.split('$')
                  if  usn == line_list[0] and pwd == line_list[1]:
                        return True
            return False
def register():
      #注册新用户
      #打开数据库，以user$password往最后追加
      status = True
      while status:
            usn,pwd = user_input()
            if if_user_exists(usn):
                  print('Existing username.Try again.')
            else:
                  status = False

      with open('C:\Python36\TEST\db','a',encoding='utf-8') as user_db:
            #文件指针在末尾，需加换行符到下一行
            temp = '\n' + usn + '$' + pwd
            user_db.write(temp)
      return True

def pwd_change():
      '''
      if 用户名存在
            if 密码正确
                  输入新密码
                  写入新密码
                  提示成功
            el 密码不正确
                  提示密码错误
                  退出
      el 用户名不存在
            提示用户不存在
            退出

      '''
      usn,pwd = user_input()
      with open('C:\Python36\TEST\db','rb+') as user_db:
            user_db.seek(0)
            for line in user_db:
                  line = line.strip()
                  line_list = line.split('$')
                  if line_list[0] == usn:
                        if pwd == line_list[1]:
                              new_pwd = str(input('Enter a new password:'))
                              line = line.replace(line_list[1],new_pwd)
                              user_db.seek(-len(line),1)
                              user_db.write(bytes(line))
                              print('Password changed.')
                              return True
                        else:
                              print('Password not mathched.Check again.')
                              return True
            print('No user found.Check the username you input.')



def erase_user():
'''
      if 用户名存在：
            if 密码正确：
                  删除用户
                  提示删除成功
            el 密码
                  提示删除失败
      el 用户名不存在：
            提示用户名不存在
'''

def main():
      print('Welcome to XX system.')
      inp = input('1:log-in\n2:register\n3:erase a user\n4.password change\n>')
      if inp == '1':
            if login_if():
                  print('Successful log-in.')
            else:
                  print('Log-in failed.')
      elif inp == '2':
            register()
            print('Successful registry.')
      elif inp == '3':
            erase_user()
      elif inp == '4':
            pwd_change()

#########################################################
#冒泡排序
li = [33,2,10,1]
for i in range(len(li)):
      print(i)
import re

#########################################################
import re
origin = '1 - 2 *( (60-30+(-40.0/5)*(9-2*5/3+7/3*99/4*2998+10*568/14))-(-4*3)/(16-3*2))'
while True:
      result = re.split('\(([^()]+)\)',origin,1)
      if len(result) == 3:
            before = result[0]
            content = result[1]
            after = result[2]
            r = eval(content)
            new_str = before + str(r) + after
            origin = new_str
      else:
            print(eval(origin))

