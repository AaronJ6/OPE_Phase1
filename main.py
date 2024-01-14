from database import execute_query
from crypto import *
from query_parser import tokenize
from display import display_table
def run_query(query):
    if query.startswith('CREATE'):
        return execute_query(query)
    tokens = tokenize(query)
    
    for token in tokens:
        if token.get('type') == 'string':
            token['token'] = '"'+str(string_encrypt(token['token']))+'"'
            #token['token'] = string_decrypt(token['token'])
        elif token.get('type') == 'number':
            token['token'] = ope_encrypt(int(token['token']))
        elif token.get('type') == 'variable':
            pass
    #print(tokens)
    
    #rebuild the query
    query = ''
    for token in tokens:
        if token['token'] == '('  or token['token'] == ',':
            query = query[:-1]
            query += token['token']
            continue
        if token['token'] == ')':
            query=query[:-1]
        
        query += str(token['token']) + ' '
    print(query)
    return execute_query(query)
    
        

if __name__ == "__main__":
    with open('test.sql', 'r') as f:
        querySet = f.read().split(';')
       
    for query in querySet:
        if query == '':
            continue
        display_table(run_query(query))
    