import pickle
import hashlib
import os

def encryp(in_str):
    md5_obj = hashlib.md5()
    md5_obj.update(bytes(in_str,encoding='utf-8'))
    encrypted_result = md5_obj.hexdigest()
    return encrypted_result
print(os.mkdir('123'))
# ek = encryp('xyf')
# ev = encryp('123')
# d = {ek:ev}
# f=open('a/' + 'user_accounts','wb')
# pickle.dump(d,f)
# f.close()

#
# f=open('user_accounts','wb')
# pickle.dump(e,f)
# f.close()
#
#
# with open('user_accounts','rb') as f:
#     dict = pickle.load(f)
#     print(dict)

# 函数定义在调用之前，如下即为反例
# class C:
#     def crack(self,a,b):
#         CreateAccount()
# c = C()
# c.crack(1,2)
#
# def CreateAccount(a,b):
#     print(a,b)
#
# d = {'a':'b'}
# print(d.__contains__('a'))
