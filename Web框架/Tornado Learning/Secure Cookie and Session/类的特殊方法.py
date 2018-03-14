class Foo:
    def __call__(self, *args, **kwargs):
        pass

    def __init__(self):
        pass

    def __class__(self):
        pass

    def __setitem__(self, key, value):
        pass

    def __getitem__(self, item):
        pass

    def __delitem__(self, key):
        pass


obj = Foo()       # __call__, __init__
obj['k1'] = 'v1'  # __setitem__
obj['k1']         # __getitem__
del obj['k1']     # __delitem__