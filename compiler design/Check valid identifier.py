import re

identifier = input("Enter identifier: ")

if re.match(r'^[A-Za-z_][A-Za-z0-9_]*$', identifier):
    print("Valid Identifier")
else:
    print("Invalid Identifier")