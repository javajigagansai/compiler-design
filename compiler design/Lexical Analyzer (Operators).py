operators = ['+', '-', '*', '/', '=', '==']

expr = input("Enter expression: ")
tokens = expr.split()

for token in tokens:
    if token in operators:
        print(token, "→ Operator")
    else:
        print(token, "→ Not Operator")