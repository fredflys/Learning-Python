import random


class BingoCage:
    def __init__(self, items):
        self._items = items
        # shuffle will work in place
        random.shuffle(self._items)

    def pick(self):
        try:
            return self._items.pop()
        except IndexError:
            raise LookupError('Pick from am empty BingoCage is not allowed.')

    def __call__(self):
        return self.pick()


bingo = BingoCage(range(10))
bingo.pick()
# same as calling pick()
bingo()
# True because __call__ is defined
callable(bingo)

