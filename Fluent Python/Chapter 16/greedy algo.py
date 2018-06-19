# we'll use decimal.Decimal for exact precision
from decimal import Decimal

# generator is returned and get unpacked
quarter, dime, nickel, penny = (Decimal(x) for x in ('0.25', '0.10', '0.05', '0.01'))

# -------------------1------------------ #
# we imagine a cash register with infinite supplies of each denomination
def change(amount):
    """
    >>> assert list(change(Decimal('0.75'))) == [quarter, quarter, quarter]
    >>> assert list(change(Decimal('0.35'))) == [quarter, dime]
    >>> assert list(change(Decimal('0.43'))) == [quarter, dime, nickel, penny, penny, penny]
    """
    returned_change = []

    # try to return as many quarters as possible:
    while sum(returned_change) + quarter <= amount:
        returned_change.append(quarter)

    # next try dimes
    while sum(returned_change) + dime <= amount:
        returned_change.append(dime)

    # nickles
    while sum(returned_change) + nickel <= amount:
        returned_change.append(nickel)

    # pennies
    while sum(returned_change) + penny <= amount:
        returned_change.append(penny)

    return returned_change


# -------------------2------------------ #
coinage = {coin for coin in [quarter, dime, nickel, penny]}


def generator_change(amount, coinage=coinage):
    """
    >>> assert list(generator_change(Decimal('0.75'))) == [quarter, quarter, quarter]
    >>> assert list(generator_change(Decimal('0.35'))) == [quarter, dime]
    >>> assert list(generator_change(Decimal('0.43'))) == [quarter, dime, nickel, penny, penny, penny]
    """
    returned_amount = Decimal('0')
    for coin in reversed(sorted(coinage)):
        while returned_amount + coin <= amount:
            yield coin
            returned_amount += coin


# -------------------3------------------ #
from itertools import repeat, chain, takewhile
lambda_greedy = lambda items, predicate: chain.from_iterable(takewhile(predicate,repeat(x)) for x in reversed(sorted(items)))


def greedy(items, predicate):
    """
    >>> assert list(greedy(coinage, pred(Decimal('0.75')))) == [quarter, quarter, quarter]
    >>> assert list(greedy(coinage, pred(Decimal('0.35')))) == [quarter, dime]
    >>> assert list(greedy(coinage, pred(Decimal('0.43')))) == [quarter, dime, nickel, penny, penny, penny]
    """
    return chain.from_iterable( # each takewhile gives a list, so let's flatten them
             takewhile(predicate,repeat(x)) # take from an infinite reservoir of items (coins)
                                            #   until we're told to stop
             for x in reversed(sorted(items))) # do this for each of the items we're
                                               #   we're allowed to pick from (coin denominations)
                                               #   and do it in reverse, sorted order (big coins to small coins)


def pred(amount, state=None):
    state = state or [] # capture the state in the closure

    def takecoin(item):
        if sum(state) + item <= amount:
            state.append(item)
            return True
        return False
    return takecoin


if __name__ == "__main__":
    print(list(generator_change(Decimal('0.75'))))
    import doctest
    doctest.testmod()