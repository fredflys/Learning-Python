import collections
from random import choice

Card = collections.namedtuple('Card', ['rank', 'suit'])


class Deck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]


deck = Deck()

# 随机抽牌
choice(deck)

# 返回牌组长度
len(deck)

# 返回前三张牌
deck[:3]

# 从第12张开始每隔13张返回一张
deck[12::13]

# iterable
for card in reversed(deck):   # doctest: +ELLIPSIS
    print(card)

Card('Q', 'hearts') in deck

# sorting: by rank(aces being highest), then by suit(spades > hearted > diamonds > clubs)
# rank_value * 4 + suit_value
suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)


def spades_high(card):
    rank_value = Deck.ranks.index(card.rank)
    return rank_value * len(suit_values) + suit_values[card.suit]


for card in sorted(deck, key=spades_high):
    print(card)