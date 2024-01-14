import tabulate
from crypto import ope_decrypt, string_decrypt
from benchmark import *
def display_table(table):
    '''
    Accepts a list of dictionaries, decrypts the values and displays it as a table
    '''
    for row in table:
        for key,value in row.items():
           #if the string is a number, decrypt it
            if isinstance(value, int) and key != 'id':
                row[key] = ope_decrypt(int(value))
            elif isinstance(value, str):
                row[key] = string_decrypt(value)
    print(tabulate.tabulate(table, headers="keys", tablefmt="psql"))
            
    
if __name__ == "__main__":
    pass