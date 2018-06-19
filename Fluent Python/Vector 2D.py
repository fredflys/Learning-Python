from array import array
import random
import math


class Vector2d:
    typecode = 'd'
    # 用__slots__用以节省空间
    # 因为字典使用哈希表进行存储，总会使用多于需要的空间
    # __slots__ = ('__x', '__y','__weakref__')

    def __init__(self, x, y):
        self.__x = float(x)
        self.__y = float(y)

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    def __iter__(self):
        return (i for i in (self.x, self.y))

    def __repr__(self):
        class_name = type(self).__name__
        return '{}({!r}, {!r})'.format(class_name, *self)

    def __str__(self):
        return str(tuple(self))

    def __bytes__(self):
        return (bytes([ord(self.typecode)])) + (bytes(array(self.typecode, self)))

    def __eq__(self, other):
        return tuple(self) == tuple(other)

    def __abs__(self):
        return math.hypot(self.x, self.y)

    def __bool__(self):
        return bool(abs(self))

    @classmethod
    def frombytes(cls, octests):
        typecode = chr(octests[0])
        memv = memoryview(octests[1:]).cast(typecode)
        return cls(*memv)

    def __format__(self, fmt_spec=''):
        if fmt_spec.endswith('p'):
            ftm_spec = fmt_spec[:-1]
            coords = (abs(self), self.angle())
            outer_fmt = '<{}, {}>'
        else:
            corrds = self
            outer_fmt = '({}, {})'
        components = (format(c, fmt_spec) for c in coords)
        return '({}, {})'.format(*components)

    def angle(self):
        return math.atan2(self.y, self.x)

    def __hash__(self):
        return hash(self.x) ^ hash(self.y)


v = Vector2d(3, 4)
print(v.__dict__)