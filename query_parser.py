from constants import *
import re


query = '''
SELECT * FROM table1 WHERE column1 = 1 AND column2 >= 2 OR column3 = 3

'''

filter = reservedWords+operators+brackets


split_pattern = re.compile(r'\s+|,|\(|\)')
tokens = re.split(split_pattern, query)
string_pattern = re.compile(r'[a-zA-Z]+')
number_pattern = re.compile(r'\d+')
strings =[]
numbers = []
for token in tokens:
    if token not in filter:
        if re.match(string_pattern, token):
            strings.append(token)
        elif re.match(number_pattern, token):
            numbers.append(token)


print(strings)
print(numbers)