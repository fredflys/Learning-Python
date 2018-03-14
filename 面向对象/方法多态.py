class calculator:
    def count(self, args):
        return 1
calc = calculator()
from random import choice
obj = choice(['string',
              [1, 2, 3],
              calc])
print (obj)
print (type(obj))
print (obj.count(''))
