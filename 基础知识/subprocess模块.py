# 用python来执行系统命令
import subprocess as sp

# 获取执行命令的返回码，用处不大
# i = sp.call('ipconfig')

# 执行命令，0则返回，否则抛出异常
# cc = sp.check_call(['ipconfig','-1'])

# 执行命令，成则返回字节形式的结果，否则抛出异常
# co = sp.check_output('ipconfig',shell=True)
# co2 = sp.check_output("['ls",'-1'],shell=False)


# 执行复杂的命令,可建立通道
spo = sp.Popen('python',stdin=sp.PIPE,stdout=sp.PIPE,stderr=sp.PIPE,universal_newlines=True)
spo.stdin.write('print(1)\n')
spo.stdin.write('print(2)\n')
#spo.stdin.write('print 3')
spo.stdin.close()

cmd_out = spo.stdout.read()
spo.stdout.close()
cmd_err = spo.stderr.read()
spo.stderr.close()

cmd_com = spox.communicate()
print(cmd_out)
print(cmd_com)
print(cmd_err)
