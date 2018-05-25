import doctest
from operator import add


def make_adder(n):
    return lambda k : n + k


# There is a general relationship between these two functions
result_1 = make_adder(3)(2)
result_2 = add(3,2)

print(result_1 == result_2)


def curry2(f):
    """
    Currying:
    Transform a multi-argument function into a single-argument higher-order function
    """
    def g(x):
        def h(y):
            return f(x, y)
        return h
    return g


curry2_lambda = lambda f: lambda x: lambda  y: f(x, y)
func = curry2(add)
add_three = func(3)
print(add_three(2))