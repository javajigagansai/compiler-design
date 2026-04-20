import re

code = input("Enter code: ")

tokens = re.findall(r'\w+|[^\s\w]', code)

for token in tokens:
    print(token)