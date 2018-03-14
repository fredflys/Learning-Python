# key=value
a = dict(one=1, two=2, three=3)
# key:value
b = {'one': 1, 'two': 2, 'three': 3}
# from two lists
c = dict(zip(['one', 'two', 'three'], [1, 2, 3]))
# from pairs in tuple
d = dict([('two', 2), ('one', 1), ('three', 3)])
# dict constructor
e = dict({'three': 3, 'one': 1, 'two': 2})
print(a == b == c == d == e)

# dict comprehensions
DIAL_CODES = [
    (86, 'China'), (91, 'India'), (1, 'United States'),
    (62, 'Indonesia'), (55, 'Brazil'), (92, 'Pakistan'),
    (880, 'Bangladesh'), (234, 'Nigeria'), (7, 'Russia'),
    (81, 'Japan')
]
country_code = {
    country: code for code, country in DIAL_CODES
}

# reverse the pair and change the country to upper case and items filtered by code < 66
another_one = {
    code: country.upper() for country, code in country_code.items() if code < 66
}