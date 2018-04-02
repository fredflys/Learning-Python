def func(name, *content, cls=None, **attrs):
    local_var = name


# parameters' default values
print(func.__defaults__)
# parameters and local variables
print(func.__code__.co_varnames)
# count argument, * and ** prefixed arguments excluded
print(func.__code__.co_argcount)

print('------------')
# Better Way
# function signature
from inspect import signature
sig = signature(func)
# signature object
print(sig)
print(type(sig))
# signature has a parameters attr
# it holds name:parameter instance pair
# parameter instance has attrs like kind and default
for name, param in sig.parameters.items():
    print(param.kind, ':', name, '=', param.default)


paras = {
    'name': 'john', 'title': 'great',
    'src': 'shot.png', 'cls': 'pic',
}
# inspect.BoundArguments object
bound_args = sig.bind(**paras)
for name, value in bound_args.arguments.items():
    print(name, '=', value)

del paras['name']
# will raise an error because 'name' parameter lack a default value
bound_args = sig.bind(**paras)
