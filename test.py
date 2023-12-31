#tokenize sql using sql glot

from sqlglot import parse
import json
import sys

def main():
    query = sys.argv[1]
    parsed = parse(query)
    print(parsed)
    parsed.pop('type', None)
if __name__ == "__main__":
    main()