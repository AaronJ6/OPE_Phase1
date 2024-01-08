#tokenizer from sqlglot
from sqlglot import Tokenizer,TokenType
#pretty print
from pprint import pprint

#tokenizer from sqlparse

tokenizer = Tokenizer()
tokens = tokenizer.tokenize("SELECT * FROM foo WHERE bar = '1' AND baz = 2")


# for token in tokens:
#     print(token.text, token.token_type)
    

#seperate numbers and strings
strings = []
numbers = []
variables = []
for token in tokens:
    if token.token_type == TokenType.STRING:
        strings.append({
            'text': token.text,
            'type': 'string'
        })
    elif token.token_type == TokenType.NUMBER:
        numbers.append({
            'text': token.text,
            'type': 'number'
        })
    elif token.token_type == TokenType.VAR:
        variables.append({
            'text': token.text,
            'type': 'variable'
        })
pprint(strings)
pprint(numbers)
pprint(variables)
        
        