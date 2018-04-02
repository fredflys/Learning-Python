def factorial(n):
    """return n!"""
    return 1 if n < 2 else n * factorial(n-1)


fact = factorial
# list of 0!...5!
list(map(fact, range(6)))
[fact(n) for n in range(6)]

# list of odd numbers factorial less than 6
# map function return a iterator in python 3 , thus convert it to a list
list(map(fact, filter(lambda n: n % 2, range(6))))
[fact(n) for n in range(6) if n % 2]
