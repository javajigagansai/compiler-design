grammar = {
    'E': ['TR'],
    'R': ['+TR', 'ε'],
    'T': ['FY'],
    'Y': ['*FY', 'ε'],
    'F': ['(E)', 'id']
}

first = {}

def find_first(symbol):
    if symbol not in grammar:
        return {symbol}
    
    result = set()
    for prod in grammar[symbol]:
        result |= find_first(prod[0])
    
    return result

for nt in grammar:
    first[nt] = find_first(nt)

print(first)