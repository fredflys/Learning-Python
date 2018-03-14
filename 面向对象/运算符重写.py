class Vector(object):
    def __init__(self,a,b):
        self.a = a
        self.b = b

    def __str__(self):
        return 'Vector (%d %d)' % (self.a, self.b)

    def __add__(self,other):
        return Vector(self.a + other.a, self.b+other.b)


x = Vector(3,7)
y = Vector(1, -10)
print(x+y)
print(str(x))
