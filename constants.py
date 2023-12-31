operators = [
    '=', '>', '<', '>=', '<=', '!=', '<>', 'LIKE',
    'IN', 'NOT IN', 'BETWEEN', 'IS NULL', 'IS NOT NULL',
    'AND', 'OR', 'NOT', '+', '-', '*', '/', '%', '||'
]

brackets = ['(', ')']

from sqlparse import keywords

reservedWords = list(keywords.KEYWORDS_COMMON) +list(keywords.KEYWORDS_ORACLE)+list(keywords.KEYWORDS_PLPGSQL)+list(keywords.KEYWORDS_HQL)+list(keywords.KEYWORDS_MSACCESS)+ list(keywords.KEYWORDS) +['*']
