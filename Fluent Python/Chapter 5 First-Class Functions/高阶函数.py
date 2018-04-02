# Sorting a list by their revered spelling
fruits = [
    'strawberry', 'fig', 'apple', 'cheery', 'raspberry', 'banana'
]


def reverse(word):
    return word[::-1]


# pass a function as an argument
sorted(fruits, key=reverse)
sorted(fruits, key=lambda word: word[::-1])
