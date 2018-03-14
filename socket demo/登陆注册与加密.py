import hashlib


def register(usn,pwd):
    accounts_path = r'd:\learning\python files\accounts'
    with open(accounts_path,'a',encoding='utf-8') as f:
        new_account = usn + '|' + md5_encrypt(pwd)
        f.write(new_account)
    return True

def logon(usn,pwd):
    accounts_path = r'd:\learning\python files\accounts'
    with open(accounts_path,'r',encoding='utf-8') as f:
        for line in f:
            u,p = line.strip().split('|')
            if usn == u and md5_encrypt(pwd) == p:
                return True

def md5_encrypt(string_for_encrypt):
    mo = hashlib.md5(b'salt')
    mo.update(bytes(string_for_encrypt,encoding='utf-8'))
    return mo.hexdigest()

def select_and_run():
    print('1.注册\n2.登陆')
    user_choice = input('请选择：')
    if user_choice == '1':
        user = input('用户名:')
        password = input('密码:')
        r_result = register(user,password)
        if r_result:
            print('注册成功')
    elif user_choice == '2':
        user = input('用户名:')
        password = input('密码:')
        l_result = logon(user,password)
        if l_result:
            print('登陆成功')
        else:
            print('登陆失败')
    else:
        print('请重选!')



select_and_run()

