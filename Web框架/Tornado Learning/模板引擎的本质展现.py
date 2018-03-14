
namespace = {
    'name': 'yeff',
    'data': [23, 24, 25, 26],
}

code = """def my_info(): return "name %s , age %d" % (name,data[0])"""

# expression是一个计算过程，为得到了一个结果
# Something which evaluates to a value. Example: 1+2/x
# statement只是一个声明，表明程序要做一些事
# Statement: A line of code which does something. Example: GOTO 100
# compile : Compile the source into a code or AST object.
func = compile(source=code, filename='<string>', mode="exec") # mode="eval" if source consists of a single expression
exec(func, namespace)
result = namespace['my_info']()
print(result)